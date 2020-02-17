from app.blueprints.main import main
from flask import render_template, redirect, url_for, flash
from app.forms import ContactForm
from app.email import send_email

@main.route('/')
def index():  
    return render_template('index.html')

@main.route('/main')
def home():
    return render_template('home.html')

@main.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    context = {
        'form' : form
    }
    if form.validate_on_submit():
        send_email()
        flash("Your form submittion was sucessful", "info")
        return redirect(url_for('main.contact'))
    return render_template('contact.html', **context)