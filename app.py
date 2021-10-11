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

from email_template import EmailTemplate
from config import Config
import models

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config.from_object(Config)

# Database
db = SQLAlchemy(app)

# Migration
migrate = Migrate(app, db)

# Models


@app.route('/')
def home():
    return render_template('landing.html', title='KLIK JEMPOL')


@app.route('/admin')
def landing():
    pendidikan = models.Pendidikan.query.all()
    provinsi = models.Prov.query.all()
    return render_template('home.html', title='KLIK JEMPOL - Admin', pendidikan=pendidikan, provinsi=provinsi)


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


@app.route('/kabkot', methods=['POST'])
def kabkot():
    kode_prov = None

    if (request.method == 'POST'):
        kode_prov = request.form['kode_prov']
        kabkot = models.Kabkot.query.filter_by(kode_prov=kode_prov).all()

        return kabkot


if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)
