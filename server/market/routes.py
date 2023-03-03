# API route
from market import app
from flask import render_template
from market.models import Item

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/about/<username>')
def about(username):
    return f'This page is about {username}'

# This is being used in client side.
@app.route('/members')
def members():
    return {'members': ['member1', 'member2', 'member3']}