from enum import unique
from Doormed import db,login_seller
from flask_login import UserMixin

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



db.create_all()