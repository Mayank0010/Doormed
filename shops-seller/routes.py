@app.route('/seller_login', methods = ['GET','POST'])
def login_seller():
    if request.method == 'POST':
        email = request.form.get("email")
        password1 = request.form.get("password")
        seller = Register_seller.query.filter_by(email = email ).first()
        
        # form.email.data = ""
        if seller and bcrypt.check_password_hash(seller.password,password1):
            return redirect(url_for('shops', id = seller.id))
        elif seller is None:
            flash(f"You haven't registered yet! Register first!")
              
        else:
            flash(f'Login Unsuccessful. Please check email or password','danger')     
            return redirect(url_for('login_seller')) 

    return render_template('sellers/login.html')    



@app.route('/shops/<int:id>')
def shops(id):
    seller = Register_seller.query.filter_by(id = id ).first()
    return render_template('sellers/shop.html', seller = seller)