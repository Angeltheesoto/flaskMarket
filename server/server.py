from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
CORS(app)


# Our models --
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable =False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    
    def __repr__(self):
        return f'Item{self.name}'

with app.app_context():
    db.create_all()

# API route
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

# When you deploy, change debug to false.
if __name__ == '__main__':
    app.run(debug=True)