from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'ed20cd685c789acaea6fdb10'
db = SQLAlchemy(app)
CORS(app)

# routes
from market import routes

# helps with database error
with app.app_context():
    db.create_all()

# When you deploy, change debug to false.
if __name__ == '__main__':
    app.run(debug=True)