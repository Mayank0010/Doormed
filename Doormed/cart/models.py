from Doormed import db
from Doormed.seller.models import Products


class Cartitem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'),nullable=False)    