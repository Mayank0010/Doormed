from enum import unique
from Doormed import db,login_seller, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Register_user.query.get(user_id)

class Register_user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    pincode = db.Column(db.String(10), unique=False, nullable=False)
    address = db.Column(db.Text,nullable=True)
    number = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    cartitems2 = db.relationship('Cartitem', backref='cust')

    def __repr__(self):
        return '<Register_user %r>' % self.name


@login_seller.user_loader
def load_seller(user_id):
    return Register_seller.query.get(user_id)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    catagory = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Numeric(10,2), nullable = False)
    mfg = db.Column(db.String(60), nullable=True)
    description = db.Column(db.Text, nullable=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('register_seller.id'),nullable=False)
    pic = db.Column(db.String, nullable=False)
    cartitems1 = db.relationship('Cartitem', backref='cart')

    def __repr__(self):
        return '<Products %r>' % self.name

class Register_seller(db.Model, UserMixin):
    __tablename__ = 'register_seller'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    number = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.Text)
    city = db.Column(db.String(80), unique=False, nullable=False)
    pincode = db.Column(db.String(10), unique=False, nullable=False)
    state = db.Column(db.String(80), unique=False, nullable=False)
    shop_name = db.Column(db.String(80), unique=False, nullable=False)
    bio = db.Column(db.String(200), unique=False, nullable=True,
                    default="This shop provide you medicines at highest discount")
    image = db.Column(db.String, nullable = False)
    product = db.relationship('Products', backref='shop', lazy=True)

    def __repr__(self):
        return '<Register_seller %r>' % self.name

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.Integer, unique=False, nullable=False)
    query = db.Column(db.Text, unique=False, nullable=False)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f"Contact('{self.name}' , '{self.email}' , '{self.phone}' , '{self.query}')"

class Cartitem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'),nullable=False) 
    customer_id = db.Column(db.Integer, db.ForeignKey('register_user.id'),nullable=False) 

db.create_all()