from enum import unique
from Doormed import db
from datetime import datetime

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.Integer, unique=False, nullable=False)
    query = db.Column(db.Text, unique=False, nullable=False)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f"Contact('{self.name}' , '{self.email}' , '{self.phone}' , '{self.query}')"

db.create_all()