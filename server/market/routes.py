# API route
from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm
from market import db

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

# route for register page
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                               email_address=form.email_address.data,
                               password_hash =form.password1.data);
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: # If there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f"There was an error with creating a user: {err_msg}", category='danger')
    return render_template('register.html', form=form)

# This is a test route to show how routes can be dynamic. 
@app.route('/about/<username>')
def about(username):
    return f'This page is about {username}'

# This is being used in client side.
@app.route('/members')
def members():
    return {'members': ['member1', 'member2', 'member3']}