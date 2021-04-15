from Doormed import app
from flask import render_template,redirect,url_for,request,flash

@app.route('/cart')
def cart():
    return render_template("cart/cart.html")