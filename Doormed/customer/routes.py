from Doormed import app, db, bcrypt
from flask import render_template,redirect,url_for,request,flash
from Doormed.models import Register_user
from flask_login import login_user, current_user, logout_user, login_required
from Doormed.models import Register_seller, Products


@app.route('/customer_page')
def customer():
    shop = Register_seller.query.all()
    return render_template("customer/shops.html", shops=shop)

@app.route('/reg_user', methods=['GET', 'POST'])
def reg_user():
    if request.method == "POST":
        name = request.form.get("Name")
        email = request.form.get("EmailID")
        address = request.form.get("Address")
        city = request.form.get("City")
        pin = request.form.get("PinCode")
        number = request.form.get("MobileNumber")
        password = request.form.get("Password")

        hash_password = bcrypt.generate_password_hash(password)
        email1 = Register_user.query.filter_by(email = email).first()
        no1 = Register_user.query.filter_by(number = number).first()
        if email1 or no1:
            flash(f'This email or phone number is already taken....Change that one')
            return redirect(url_for('reg_user'))

        entry = Register_user(name=name, email=email,address=address, city=city.lower(), pincode=pin, number=number, password=hash_password)
        db.session.add(entry)
        db.session.commit()
        flash(f'{name} you are registered successfully in our database ', 'success')
        return redirect(url_for('user_login'))
    return render_template("customer/Registration-C.html")

@app.route('/user_login', methods = ['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        email = request.form.get("loginid")
        password1 = request.form.get("pass")
        customer = Register_user.query.filter_by(email = email ).first()
        
        # form.email.data = ""
        if customer and bcrypt.check_password_hash(customer.password,password1):
            # return redirect(url_for('shops', id = seller.id))
            login_user(customer)
            return redirect(url_for('main', id=customer.id))
        elif customer is None:
            flash(f"You haven't registered yet! Register first!")
              
        else:
            flash(f'Login Unsuccessful. Please check email or password','danger')     
            return redirect(url_for('user_login')) 

    return render_template("customer/login_user.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('customer'))

@app.route('/main/<int:id>')
@login_required
def main(id):
    user = Register_user.query.filter_by(id = id).first()
    pros = []
    shop1 = []
    q = request.args.get('q')
    if q:
        shops1 = Register_seller.query.filter_by(city=user.city.lower()).all()
        for sho in shops1:
            prod = Products.query.filter_by(shop_id=sho.id).all()           
            for p in prod:
                if q.lower() in p.name.lower():
                    pros.append(p)
                    shop1.append(sho)
                # pros = Products.query.filter(Products.name.contains(q))
                # shops.append(shops1)
        return render_template('customer/searchmed.html', shop_and_prod = zip(shop1,pros), products=pros,shop=shop1,q=q,id=id)
    else:
        shops = Register_seller.query.filter_by(city = user.city.lower())
    return render_template('customer/index.html', shops = shops, user = user)

@app.route('/main/<int:id>/search',methods=['GET','POST'])
def search(id):
    user = Register_user.query.filter_by(id = id).first()
    pros = []
    shop1 = []
    q = request.args.get('q')
    if q:
        shops1 = Register_seller.query.filter_by(city=user.city.lower()).all()
        for sho in shops1:
            prod = Products.query.filter_by(shop_id=sho.id).all()           
            for p in prod:
                if q.lower() in p.name.lower():
                    pros.append(p)
                    shop1.append(sho)
                # pros = Products.query.filter(Products.name.contains(q))
                # shops.append(shops1)
        return render_template('customer/searchmed.html', shop_and_prod = zip(shop1,pros), products=pros,shop=shop1,q=q,id=id)
    return redirect(url_for('main',id=id))

@app.route('/<string:name>')
@login_required
def shop_details(name):
    shop = Register_seller.query.filter_by(shop_name = name ).first()
    products = Products.query.filter_by(shop_id = shop.id)
    return render_template("customer/medlist.html", shop=shop, products=products)

@app.route('/<string:name>')
@login_required
def medicine(name):
    products = Products.query.filter_by(name=name)
    shop = Register_seller.query.filter_by(id = products.shop_id)
    return render_template("searchmed.html",products=products, shops=shop)

@app.route('/main/<int:id>/account')
@login_required
def account(id):
    user = Register_user.query.filter_by(id=id).first()
    return render_template("customer/account.html",user=user)

@app.route('/main/<int:id>/account/update',methods=['GET','POST'])
@login_required
def update(id):
    user = Register_user.query.filter_by(id=id).first()
    if request.method == 'POST':
        user.email = request.form.get('email')
        user.number = request.form.get('num')
        user.address = request.form.get('add')
        user.city = request.form.get('city')
        db.session.commit()
        return redirect(url_for('account',id=id))
    return render_template("customer/account.html",user=user)

