from Doormed import app,db
from flask_login import current_user
from flask import render_template
from Doormed.models import Register_user,Register_seller,Products
from Doormed import admin
from flask_admin.contrib.sqla import ModelView


admin.add_view(ModelView(Register_seller, db.session))
admin.add_view(ModelView(Register_user, db.session))
admin.add_view(ModelView(Products, db.session))

@app.route('/')
def index():
    if current_user.is_authenticated:
        user = Register_user.query.filter_by(id=current_user.id).first()
        if user:
            return render_template("main/home.html", id=user.id)
    return render_template("main/home.html")
