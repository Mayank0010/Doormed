from Doormed import app
from flask import render_template,redirect,url_for,request,flash

@app.route('/')
def index():
    return render_template("main/home.html")

