from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'ed20cd685c789acaea6fdb10'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

# routes
from market import routes

# helps with database error
with app.app_context():
    db.create_all()

# When you deploy, change debug to false.
if __name__ == '__main__':
    app.run(debug=True)