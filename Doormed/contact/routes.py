from Doormed import app,db, mail
from Doormed.models import Contact
from flask import render_template,redirect,url_for,request,flash
from threading import Thread
from flask_mail import Mail, Message
from datetime import datetime

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to,subject,template,**kwargs):
    msg=Message(app.config['MAIL_SUBJECT_PREFIX']+subject,sender=app.config['MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return thr


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        query = request.form.get('query')
    
        details = Contact(name=name, email=email, phone=phone, query=query, date=datetime.now())
        db.session.add(details)
        db.session.commit()
        if app.config['ADMIN']:
            send_mail(app.config['ADMIN'],'New Query/Message','mail/query',name=name,email=email,phone=phone,query=query)
            flash(f'{name}, Your query is submitted...we will get back to you soon!!', 'success')
            return redirect(url_for('contact'))
    return render_template("contact/contact.html")


# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db,Contact=Contact)