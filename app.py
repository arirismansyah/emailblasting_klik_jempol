from enum import unique
from genericpath import isdir
import smtplib
import ssl

import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import os
import pandas as pd
import numpy as np
import xlsxwriter
import base64
import json
from datetime import datetime, time
import json

from flask import Flask, app, redirect, url_for, stream_with_context, render_template, Response, jsonify, request, make_response, send_file, send_from_directory, session
from flask_ngrok import run_with_ngrok
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect

from email_template import EmailTemplate
from config import Config

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config.from_object(Config)

# Database
db = SQLAlchemy(app)

# Migration
migrate = Migrate(app, db)

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
        'prov.kode_prov'), nullable=False)
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
    email = db.Column(db.String(200), nullable=True, unique=True)
    tempat_lahir = db.Column(db.String(200), nullable=True)
    tanggal_lahir = db.Column(db.Date, nullable=True)
    pendidikan = db.Column(db.Integer, db.ForeignKey(
        'pendidikan.id_pendidikan'), nullable=True)
    pekerjaan = db.Column(db.String(200), nullable=True)
    jenis_pekerjaan = db.Column(db.Integer, db.ForeignKey(
        'pekerjaan.id_pekerjaan'), nullable=True)
    instansi = db.Column(db.String(200), nullable=True)
    alamat_domisili = db.Column(db.Text, nullable=True)
    prov_domisili = db.Column(db.Integer, db.ForeignKey(
        'prov.kode_prov'), nullable=True)
    kab_domisili = db.Column(db.Integer, db.ForeignKey(
        'kabkot.id_kabkot'), nullable=True)

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
        'status.id_status'), nullable=False, default=0)

    def __repr__(self):
        return '<Template {}>'.format(self.subject)

# # Model Log
class Log(db.Model, Serializer):
    id_log = db.Column(db.Integer, primary_key=True)
    template_email = db.Column(
        db.Integer, db.ForeignKey('template.id_template'))
    customer = db.Column(db.Integer, db.ForeignKey('customer.id_customer'))
    send_at = db.Column(db.DateTime, default=datetime.now)

# # Model FAQ
class Faq(db.Model, Serializer):
    id_faq = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)

    def __repr__(self):
        return '<FAQ {}>'.format(self.question)



@app.route('/')
def home():
    pendidikan = Pendidikan.query.all()
    jenis_pekerjaan = Pekerjaan.query.all()
    provinsi = Prov.query.all()
    return render_template('landing.html', title='KLIK JEMPOL', pendidikan=pendidikan, provinsi=provinsi, jenis_pekerjaan=jenis_pekerjaan)


@app.route('/admin')
def landing():
    pendidikan = Pendidikan.query.all()
    jenis_pekerjaan = Pekerjaan.query.all()
    provinsi = Prov.query.all()
    customers = Customer.query.all()
    return render_template('home.html', title='KLIK JEMPOL - Admin', pendidikan=pendidikan, provinsi=provinsi, jenis_pekerjaan=jenis_pekerjaan, customers = customers)


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route('/download_template', methods=['GET', 'POST'])
def download_template():
    path = 'static/template/template.xlsx'
    return send_file(path, attachment_filename='template.xlsx', as_attachment=True)


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
                os.path.join(folder_target, file_name))

            for customer in df_customers.iterrows():
                print(customer['nama'])

        return make_response('success', 200)


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
        db.session.commit()

        return make_response('success', 200)
    except:
        return make_response('register failed', 200)


@app.route('/edit_customer', methods=['POST'])
def edit_customer():
    pass


@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    pass


@app.route('/add_template', methods=['POST'])
def add_template():
    pass


@app.route('/edit_template', methods=['POST'])
def edit_template():
    pass


@app.route('/delete_template', methods=['POST'])
def delete_template():
    pass


@app.route('/send', methods=['POST'])
def send():
    pass


@app.route('/kabkot', methods=['POST'])
def kabkot():
    kode_prov = None

    if (request.method == 'POST'):
        kode_prov = request.form['kode_prov']
        kabkot = Kabkot.query.filter_by(kode_prov=kode_prov).all()
        serialized_kabkot =  Kabkot.serialize_list(kabkot)

        return jsonify(serialized_kabkot)


if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)
