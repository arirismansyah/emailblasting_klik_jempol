from enum import unique
from genericpath import isdir
from re import template
import smtplib
import ssl

import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import os
import pandas as pd
import numpy as np
import xlsxwriter
import base64
import json
from datetime import datetime
import time
import json
import threading
import random
from decimal import Decimal

from flask import Flask, app, redirect, url_for, flash, stream_with_context, render_template, Response, jsonify, request, make_response, send_file, send_from_directory, session
from flask_ngrok import run_with_ngrok
from flask_migrate import Migrate
from werkzeug.utils import html, secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect

from email_template import EmailTemplate
from config import Config

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config.from_object(Config)
# run_with_ngrok(app)

exporting_threads = {}

send_threads = {}

# Database
db = SQLAlchemy(app)

# Migration
migrate = Migrate(app, db)

# Send Email Thread
class SendMailThread(threading.Thread):
    def __init__(self, customers, template):
        self.progress = 0
        self.success_send = 0
        self.failed_send = 0
        self.customers = customers
        self.template = template
        super().__init__()
    
    def run(self):
        total = len(self.customers)
        for customer in self.customers:
            message = MIMEMultipart()
            message['From'] = Config.EMAIL
            message['To'] = customer['email']
            message['Subject'] = self.template['subject']

            email_template = EmailTemplate(receiver=customer['nama'], body=self.template['body'], product=self.template['nama_produk'], attachment=self.template['lampiran'])

            email_template_html = email_template.create_template()

            part_html = MIMEText(email_template_html, 'html')
            message.attach(part_html)

            text_mail = message.as_string()

            context = ssl.create_default_context()
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                    server.login(Config.EMAIL, Config.PASSWORD_EMAIL)
                    server.sendmail(Config.EMAIL, customer['email'], text_mail)
                
                input_log = Log(
                    template_email = self.template['id_template'],
                    customer = customer['id_customer'],
                    status = 1,
                )
            except:
                input_log = Log(
                    template_email = self.template['id_template'],
                    customer = customer['id_customer'],
                    status = 2,
                )

                db.session.add(input_log)
                db.session.commit()
                self.failed_send += 1
            else:
                db.session.add(input_log)
                db.session.commit()
                self.success_send += 1

            self.progress =+ ((self.success_send+self.failed_send)/total)*100
            
            if((self.success_send!=0) and (self.success_send % 500)==0):
                time.sleep(60*60*24)

            if(self.success_send+self.failed_send == total):
                try:
                    update_template = Template.query.get_or_404(self.template['id_template'])
                    update_template.status = 1
                    db.session.commit()
                except:
                    update_template = Template.query.get_or_404(self.template['id_template'])
                    update_template.status = 2
                    db.session.commit()
            

# Exporting Thread


class ExportingThread(threading.Thread):
    def __init__(self, df_customers):
        self.progress = 0
        self.df_customers = df_customers
        super().__init__()

    def run(self):
        total = len(self.df_customers)
        success_input = 0
        failed_input = 0

        for index, customer in self.df_customers.iterrows():
            if(customer['tanggal_lahir']!=None) and (customer['tanggal_lahir']!=""):
                tanggal_lahir = customer['tanggal_lahir'].strftime('%Y-%m-%d')
            else:
                tanggal_lahir = None

            input_customer = Customer(
                nama=customer['nama'],
                jenis_kelamin=customer['jenis_kelamin'],
                tempat_lahir=customer['tempat_lahir'],
                tanggal_lahir=tanggal_lahir,
                pendidikan=customer['pendidikan'],
                jenis_pekerjaan=customer['jenis_pekerjaan'],
                pekerjaan=customer['pekerjaan'],
                instansi=customer['instansi'],
                email=customer['email'],
                phone=customer['phone'],
                prov_domisili=customer['prov_domisili'],
                kab_domisili=customer['kab_domisili'],
                alamat_domisili=customer['alamat_domisili'],
            )

            try:
                db.session.add(input_customer)
            except:
                failed_input += 1
            else:
                db.session.commit()
                success_input += 1

            self.progress =+ ((success_input+failed_input)/total)*100


# Serialize Class
class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


# Models for Database
# # Model Pendidikan
class Pendidikan(db.Model, Serializer):
    id_pendidikan = db.Column(db.Integer, primary_key=True)
    tingkat_pendidikan = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Pendidikan {}>'.format(self.tingkat_pendidikan)

# # Model Pekerjaan


class Pekerjaan(db.Model, Serializer):
    id_pekerjaan = db.Column(db.Integer, primary_key=True)
    jenis_pekerjaan = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Pekerjaan {}>'.format(self.jenis_pekerjaan)

# # Model Provinsi Domisili


class Prov(db.Model, Serializer):
    kode_prov = db.Column(db.Integer, primary_key=True)
    nama_prov = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return 'Provinsi {}'.format(self.nama_prov)

# # Model Kab/Kota Domisili


class Kabkot(db.Model, Serializer):
    id_kabkot = db.Column(db.Integer, primary_key=True)
    kode_prov = db.Column(db.Integer, db.ForeignKey(
        'prov.kode_prov', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    nama_kabkot = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Kabupaten/Kota {}>'.format(self.nama_kabkot)

# # Model Status


class Status(db.Model, Serializer):
    id_status = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Status {}>'.format(self.nama_kabkot)

# # Model Customer


class Customer(db.Model, Serializer):
    id_customer = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(200), nullable=False)
    jenis_kelamin = db.Column(db.String(1), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(200), nullable=True)
    tempat_lahir = db.Column(db.String(200), nullable=True)
    tanggal_lahir = db.Column(db.Date, nullable=True)
    pendidikan = db.Column(db.Integer, db.ForeignKey(
        'pendidikan.id_pendidikan', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    pekerjaan = db.Column(db.String(200), nullable=True)
    jenis_pekerjaan = db.Column(db.Integer, db.ForeignKey(
        'pekerjaan.id_pekerjaan', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    instansi = db.Column(db.String(200), nullable=True)
    alamat_domisili = db.Column(db.Text, nullable=True)
    prov_domisili = db.Column(db.Integer, db.ForeignKey(
        'prov.kode_prov', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    kab_domisili = db.Column(db.Integer, db.ForeignKey(
        'kabkot.id_kabkot', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)

    # create string
    def __repr__(self):
        return '<Customer {}>'.format(self.nama)

# # Model Template Email


class Template(db.Model, Serializer):
    id_template = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    nama_produk = db.Column(db.String(200), nullable=False)
    lampiran = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Integer, db.ForeignKey(
        'status.id_status', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, default=0)

    def __repr__(self):
        return '<Template {}>'.format(self.subject)

# # Model Log


class Log(db.Model, Serializer):
    id_log = db.Column(db.Integer, primary_key=True)
    template_email = db.Column(
        db.Integer, db.ForeignKey('template.id_template'))
    customer = db.Column(db.Integer, db.ForeignKey('customer.id_customer', ondelete='CASCADE', onupdate='CASCADE'))
    status = db.Column(db.Integer, db.ForeignKey('status.id_status', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, default=0)
    send_at = db.Column(db.DateTime, default=datetime.now)

# # Model FAQ


class Faq(db.Model, Serializer):
    id_faq = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)

    def __repr__(self):
        return '<FAQ {}>'.format(self.question)

# # Model Admin
class Admin(db.Model, Serializer):
    id_admin = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))

    def __repr__(self):
        return '<Admin {}>'.format(self.username)

@app.route('/')
def home():
    pendidikan = Pendidikan.query.all()
    jenis_pekerjaan = Pekerjaan.query.all()
    provinsi = Prov.query.all()
    all_kabkot = Kabkot.query.all()
    all_faq = Faq.query.all()

    return render_template('landing.html', title='KLIK JEMPOL', pendidikan=pendidikan, provinsi=provinsi, jenis_pekerjaan=jenis_pekerjaan, all_kabkot=all_kabkot, faq=all_faq)


@app.route('/admin')
def admin():
    if 'loggedin' in session:
        pendidikan = Pendidikan.query.all()
        jenis_pekerjaan = Pekerjaan.query.all()
        provinsi = Prov.query.all()
        customers = Customer.query.all()
        all_kabkot = Kabkot.query.all()
        all_templates = Template.query.all()
        all_faq = Faq.query.all()
        jumlah_customers = len(customers)

        template_not_send = Template.query.filter_by(status=0)

        return render_template('home.html', title='KLIK JEMPOL - Admin', pendidikan=pendidikan, provinsi=provinsi, jenis_pekerjaan=jenis_pekerjaan, customers=customers, all_kabkot=all_kabkot, all_templates=all_templates, faq=all_faq, jumlah_customers = jumlah_customers, template_not_send=template_not_send)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']

        admin = Admin.query.filter_by(username=username).first()
        if ((admin != None)):
            if(password == admin.password):
                session['loggedin'] = True
                session['username'] = admin.username
                return redirect(url_for('admin'))
            else:
                flash("Username/password salah!", "error")
                return render_template('login.html')    
        else:
                flash("Username/password salah!", "error")
                return render_template('login.html')                
    else:
        return render_template('login.html', title='KLIK JEMPOL - Login')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/download_template', methods=['GET', 'POST'])
def download_template():
    path = 'static/template/template.xlsx'
    return send_file(path, attachment_filename='template.xlsx', as_attachment=True)

# Route for Customer
@app.route('/upload_customers', methods=['GET', 'POST'])
def upload_customers():
    if request.method == 'POST':
        folder_target = os.path.join(APP_ROOT, 'static', 'upload_customers')
        if (not os.path.isdir(folder_target)):
            os.mkdir(folder_target)

        # get file
        file_customer = request.files.get('file_customers')

        if(file_customer.filename.endswith('.xlsx')):
            file_name = datetime.strftime(
                datetime.now(), '%Y%m%d%H%M%S')+'_data_customers.xlsx'
            file_customer.save(os.path.join(folder_target, file_name))
            df_customers = pd.read_excel(
                os.path.join(folder_target, file_name), dtype={
                    'phone':str,
                })

            df_customers = df_customers.astype(
                object).where(pd.notnull(df_customers), None)           

            global exporting_threads

            thread_id = random.randint(0, 10000)
            exporting_threads[thread_id] = ExportingThread(df_customers)
            exporting_threads[thread_id].start()

            return {'thread_id':thread_id, 'rows':len(df_customers)}

@app.route('/progress_insert/<int:thread_id>')
def progress(thread_id):
    def make_prog():
        global exporting_threads
        yield "data:"+str(round(exporting_threads[thread_id].progress,1))+"\n\n"

    return Response(make_prog(), mimetype='text/event-stream')

@app.route('/register_customer', methods=['POST'])
def register_customer():
    customer = Customer(
        nama=request.form['name'],
        jenis_kelamin=request.form['radioJk'],
        tempat_lahir=request.form['tempat_lahir'],
        tanggal_lahir=request.form['tgl_lahir'],
        pendidikan=request.form['pendidikan'],
        jenis_pekerjaan=request.form['j_pekerjaan'],
        pekerjaan=request.form['pekerjaan'],
        instansi=request.form['instansi'],
        email=request.form['email'],
        phone=request.form['phone-val'],
        prov_domisili=request.form['dom_prov'],
        kab_domisili=request.form['dom_kab'],
        alamat_domisili=request.form['alamat'],
    )

    try:
        db.session.add(customer)
    except:
        return make_response('Register failed. Pastikan customer/email belum terdaftar.', 200)
    else:
        db.session.commit()
        return make_response('success', 200)

@app.route('/update_customer', methods=['POST'])
def update_customer():
    id_customer = request.form['id_customer']
    customer = Customer.query.get_or_404(id_customer)

    try :
        customer.nama=request.form['name']
        customer.jenis_kelamin=request.form['radioJk']
        customer.tempat_lahir=request.form['tempat_lahir']
        customer.tanggal_lahir=request.form['tgl_lahir']
        customer.pendidikan=request.form['pendidikan']
        customer.jenis_pekerjaan=request.form['j_pekerjaan']
        customer.pekerjaan=request.form['pekerjaan']
        customer.instansi=request.form['instansi']
        customer.email=request.form['email']
        customer.phone=request.form['phone-val']
        customer.prov_domisili=request.form['dom_prov']
        customer.kab_domisili=request.form['dom_kab']
        customer.alamat_domisili=request.form['alamat']
        db.session.commit()
        return make_response('success', 200)
    except:
        return make_response('failed', 200)

@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    id_customer = request.form['id_customer']
    customer = Customer.query.get_or_404(id_customer)
    try:
        db.session.delete(customer)
        db.session.commit()
        return make_response('success', 200)
    except:
        return make_response('delete failed', 200)


# Route for Template
@app.route('/add_template', methods=['POST'])
def add_template():
    template_email = Template(
        subject = request.form['subject'],
        nama_produk = request.form['nama_produk'],
        lampiran = request.form['lampiran'],
        body = request.form['body-email'],
    )

    try:
        db.session.add(template_email)
        db.session.commit()
        return ('success', 200)
    except:
        return ('failed', 200)

@app.route('/edit_template', methods=['POST'])
def edit_template():
    id_template = request.form['id_template']
    template = Template.query.get_or_404(id_template)

    try:
        template.subject = request.form['subject']
        template.nama_produk = request.form['nama_produk']
        template.lampiran = request.form['lampiran']
        template.body = request.form['body-email']
        db.session.commit()
        return make_response('success', 200)
    except:
        return make_response('failed', 200)

@app.route('/delete_template', methods=['POST'])
def delete_template():
    id_template = request.form['id_template']
    template = Template.query.get_or_404(id_template)
    try:
        db.session.delete(template)
        db.session.commit()
        return make_response('success', 200)
    except:
        return make_response('delete failed', 200)

# Route for FAQ
@app.route('/add_faq', methods=['POST'])
def add_faq():
    faq = Faq(
        question = request.form['question'],
        answer = request.form['answer'],
    )
    try:
        db.session.add(faq)
        db.session.commit()
        return ('success', 200)
    except:
        return ('failed', 200)

@app.route('/edit_faq', methods=['POST'])
def edit_faq():
    id_faq = request.form['id_faq']
    faq = Faq.query.get_or_404(id_faq)

    try:
        faq.question = request.form['question']
        faq.answer = request.form['answer']
        db.session.commit()
        return make_response('success', 200)
    except:
        return make_response('failed', 200)

@app.route('/delete_faq', methods=['POST'])
def delete_faq():
    id_faq = request.form['id_faq']
    faq = Faq.query.get_or_404(id_faq)
    try:
        db.session.delete(faq)
        db.session.commit()
        return make_response('success', 200)
    except:
        return make_response('delete failed', 200)


@app.route('/send', methods=['POST'])
def send():
    if (request.method == 'POST'):
        id_template = request.form['id_template']
        template = Template.query.get_or_404(id_template)
        customers = Customer.query.filter((Customer.email!=None)|(Customer.email!="")).all()
        serialized_customers = Customer.serialize_list(customers)
        serialized_template = Template.serialize(template)

        global send_threads
        thread_id = random.randint(0, 10000)
        send_threads[thread_id] = SendMailThread(customers=serialized_customers, template=serialized_template)
        send_threads[thread_id].start()

        return {'thread_id':thread_id, 'rows':len(serialized_customers)}



@app.route('/progress_send/<int:thread_id>')
def progress_send(thread_id):
    def make_prog():
        global send_threads
        yield "data:"+str({"progress":round(send_threads[thread_id].progress,1), "success_send":send_threads[thread_id].success_send, "failed_send":send_threads[thread_id].failed_send})+"\n\n"

    return Response(make_prog(), mimetype='text/event-stream')

@app.route('/get_template', methods=['POST'])
def get_template():
    id_template = None

    if(request.method == 'POST'):
        id_template = request.form['id_template']
        template = Template.query.get_or_404(id_template)
        serialized_template = Template.serialize(template)

        return jsonify(serialized_template)

@app.route('/kabkot', methods=['POST'])
def kabkot():
    kode_prov = None

    if (request.method == 'POST'):
        kode_prov = request.form['kode_prov']
        kabkot = Kabkot.query.filter_by(kode_prov=kode_prov).all()
        serialized_kabkot = Kabkot.serialize_list(kabkot)

        return jsonify(serialized_kabkot)

@app.route('/get_customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    serialized_customer = Customer.serialize_list(customers)

    return jsonify(serialized_customer)


if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)
    # app.run()
