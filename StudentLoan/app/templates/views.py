from flask import render_template, redirect, url_for
from app import app
from datetime import datetime
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

