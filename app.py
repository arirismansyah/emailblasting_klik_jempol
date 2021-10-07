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
import mysql.connector
import base64
import json
from datetime import time
import json

from flask import Flask, app, redirect, url_for, stream_with_context, render_template, Response, jsonify, request, make_response, send_file, send_from_directory, session
from flask_ngrok import run_with_ngrok
import flask_mysqldb
import flask_migrate
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

from email_template import EmailTemplate

app = Flask(__name__)
app.secret_key = 'klik-jempol'

@app.route('/')
def landing():
    return render_template('home.html', title='Landing')

@app.route('/tools')
def home():
    return render_template('home.html', title='Tools')

if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)