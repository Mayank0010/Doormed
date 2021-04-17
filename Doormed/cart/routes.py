from Doormed import app,db
from flask import render_template,redirect,url_for,request,flash
from Doormed.models import Register_user,Register_seller, Products, Cartitem


@app.route('/main/<int:id>/cart')
def cart(id):
    items = []
    cart1 = []
    user = Register_user.query.filter_by(id=id).first()
    carts = Cartitem.query.filter_by(customer_id=id).all()
    for cart in carts:
        item = Products.query.filter_by(id=cart.product_id).first()
        items.append(item)
        cart1.append(cart)
    # cart = Cartitem.query.filter
    return render_template("cart/cart.html",user=user,carts=carts,items=zip(items,cart1))

@app.route('/main/<int:id>/addcart',methods=['GET','POST'])
def addcart(id):
    user = Register_user.query.filter_by(id=id).first()
    product_id = request.form.get('pro_id')
    product = Products.query.filter_by(id=product_id).first()
    if request.method == 'POST':
        quantity = request.form.get('quantity')
        entry = Cartitem(quantity=quantity, product_id=product.id, customer_id=user.id)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('search',id=id))
    return redirect(url_for('search',id=id))
