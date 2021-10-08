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

from email_template import EmailTemplate

from config import Config

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)


@app.route('/')
def landing():
    return render_template('home.html', title='Landing')

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

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
        return make_response('success', 200)


@app.route('/tools')
def home():
    return render_template('landing.html', title='Tools')

if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)