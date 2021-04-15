from Doormed import app, db, bcrypt, migrate
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, current_user, logout_user, login_required
from .models import Register_seller,Products


@app.route('/reg_seller', methods=['GET', 'POST'])
def reg_seller():
    if request.method == "POST":
        name = request.form.get("Name")
        email = request.form.get("EmailID")
        password = request.form.get("Password")
        number = request.form.get("MobileNumber")
        address = request.form.get("Address")
        city = request.form.get("City")
        pin = request.form.get("PinCode")
        state = request.form.get("State")
        shop = request.form.get("shop")
        bio = request.form.get("Bio")
        image = request.form.get("fileupload")

        hash_password = bcrypt.generate_password_hash(password)

        entry = Register_seller(name=name, email=email, password=hash_password,
                                number=number, address=address, city=city,
                                pincode=pin, state=state, shop_name=shop, bio=bio, image=image)
        db.session.add(entry)
        db.session.commit()
        flash(f'{shop} is registered successfully in our database ', 'success')
        return redirect(url_for('seller_user'))
    return render_template("seller/Registration-S.html")


@app.route('/seller_login', methods=['GET','POST'])
def seller_user():
    if request.method == "POST":
        email = request.form.get("loginid")
        password = request.form.get("pass")
        seller = Register_seller.query.filter_by(email=email).first()
        if seller and bcrypt.check_password_hash(seller.password, password):
            login_user(seller)
            return redirect(url_for('shops'))
        elif seller is None:
            flash(f"You haven't registered yet! Register first!")
              
        else:
            flash(f'Login Unsuccessful. Please check email or password','danger')     
            return redirect(url_for('seller_user')) 
    return render_template("seller/login_seller.html")

@app.route('/logout_seller')
def logout_seller():
    logout_user()
    return redirect(url_for('seller_user'))


@app.route('/shops')
@login_required
def shops():
    seller = Register_seller.query.filter_by(id = current_user.id ).first()
    products = Products.query.filter_by(shop_id = current_user.id)
    return render_template('seller/shop.html', seller = seller, products=products)

@app.route('/shops/addproduct', methods=['GET','POST'])
def addprod():
    if request.method == "POST":
        name = request.form.get('Name')
        desc = request.form.get('Desc')
        image = request.form.get('Image')
        catagory = request.form.get('Catagory')
        price = request.form.get('price')
        mfg = request.form.get('Mfg')

        entry = Products(name=name, shop_id=current_user.id, catagory=catagory, price=price, mfg=mfg, description=desc, pic=image)
        db.session.add(entry)
        db.session.commit()
        flash(f'{name} is added successfully')
        return redirect(url_for('addprod'))
    return render_template("product/add.html")

@app.route('/shops/deleteproduct/<int:id>', methods=['GET','POST'])
def deleteproduct(id):
    product = Products.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(product)
        db.session.commit()
        flash(f'{product.name} deleted successfully')
        return redirect(url_for('shops'))
    return redirect(url_for('shops'))

