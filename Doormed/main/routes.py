from Doormed import app
from flask_login import current_user
from flask import render_template
from Doormed.models import Register_user


@app.route('/')
def index():
    if current_user.is_authenticated:
        user = Register_user.query.filter_by(id=current_user.id).first()
        if user:
            return render_template("main/home.html", id=user.id)
    return render_template("main/home.html")
