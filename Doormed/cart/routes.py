from Doormed import app
from flask import render_template,redirect,url_for,request,flash

@app.route('/main/<int:id>/cart')
def cart(id):
    return render_template("cart/cart.html")