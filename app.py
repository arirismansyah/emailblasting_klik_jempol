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
import flask_migrate
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

from email_template import EmailTemplate

from config import Config

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config.from_object(Config)

# Database
db = SQLAlchemy(app)

class Pendidikan(db.Model):
    id_pendidikan = db.Column(db.Integer, primary_key=True)
    tingkat_pendidikan = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Pendidikan {}>'.format(self.tingkat_pendidikan)

class Pekerjaan(db.Model):
    id_pekerjaan = db.Column(db.Integer, primary_key=True)
    jenis_pekerjaan = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Pekerjaan {}>'.format(self.jenis_pekerjaan)

class Prov(db.Model):
    kode_prov = db.Column(db.Integer, primary_key=True)
    nama_prov = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return 'Provinsi {}'.format(self.nama_prov)

class Kabkot(db.Model):
    id_kabkot = db.Column(db.Integer, primary_key=True)
    kode_prov = db.Column(db.Integer, db.ForeignKey('prov.kode_prov'), nullable=False)
    nama_kabkot = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Kabupaten/Kota {}>'.format(self.nama_kabkot)

class Status(db.Model):
    id_status = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Status {}>'.format(self.nama_kabkot)

class Customer(db.Model):
    id_customer = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(200), nullable=False)
    jenis_kelamin = db.Column(db.String(1), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(200), nullable=True, unique=True)
    tempat_lahir = db.Column(db.String(200), nullable=True)
    tanggal_lahir = db.Column(db.Date, nullable=True)
    pendidikan = db.Column(db.Integer, db.ForeignKey('pendidikan.id_pendidikan'), nullable=True)
    pekerjaan = db.Column(db.String(200), nullable=True)
    jenis_pekerjaan = db.Column(db.Integer, db.ForeignKey('pekerjaan.id_pekerjaan'), nullable=True)
    instansi = db.Column(db.String(200), nullable=True)
    alamat_domisili = db.Column(db.Text, nullable=True)
    prov_domisili = db.Column(db.Integer, db.ForeignKey('prov.kode_prov'), nullable=True)
    kab_domisili = db.Column(db.Integer, db.ForeignKey('kabkot.id_kabkot'), nullable=True)

    # create string
    def __repr__(self):
        return '<Customer {}>'.format(self.nama)

class Template(db.Model):
    id_template = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    nama_produk = db.Column(db.String(200), nullable=False)
    lampiran = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<Template {}>'.format(self.subject)


@app.route('/')
def home():
    return render_template('landing.html', title='KLIK JEMPOL')

@app.route('/admin')
def landing():
    
    return render_template('home.html', title='KLIK JEMPOL - Admin')

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

@app.route('/download_template', methods=['GET', 'POST'])
def download_template():
    path = 'static/template/template.xlsx'
    return send_file(path, attachment_filename='template.xlsx', as_attachment=True)

@app.route('/upload_customers', methods=['GET', 'POST'])
def upload_customers():
    if request.method == 'POST' :
        folder_target = os.path.join(APP_ROOT, 'static', 'upload_customers')
        if (not os.path.isdir(folder_target)):
            os.mkdir(folder_target)
        
        # get file
        file_customer = request.files.get('file_customers')
        
        if(file_customer.filename.endswith('.xlsx')):
            file_name = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')+'_data_customers.xlsx'
            file_customer.save(os.path.join(folder_target, file_name))
            df_customers = pd.read_excel(os.path.join(folder_target, file_name))

            for customer in df_customers.iterrows() :
                print(customer['nama'])


        return make_response('success', 200)


@app.route('/register_customer', methods=['POST'])
def register_customers():
    print(request.form['name'])
    return make_response('success', 200)

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

if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)