from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# API route
@app.route('/')
def home_page():
    return render_template('home.html')

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