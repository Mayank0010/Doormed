from Doormed import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Register_user.query.get(user_id)

class Register_user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    pincode = db.Column(db.String(10), unique=False, nullable=False)
    number = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Register_user %r>' % self.name

db.create_all()