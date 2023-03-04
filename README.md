# flaskMarket

<!--
create a virtual environment [python3 -m venv venv]
activate virtual environment in server with [source venv/scripts/activate]
run server [python server.py]
run client [npm start]

!NPM PACKAGES
[create-react-app] = frontend web app library.
[axios] =

!PIP PACKAGES
[pip install flask] = backend web app framework.
[pip install -U flask-cors] =
[pip install flask sqlalchemy] =
 -->

<!--
?Enter python shell
>>> python

?Create the db
>>> from server import app, db
>>> app.app_context().push()
>>> db.create_all()

?Create an item in the db
>>> from server import Item
>>> item1 = Item(name="IPhone 10", price=500, barcode="298729348453", description='desc')
>>> db.session.add(item1)
>>> db.session.commit()

?Check if your item was stored.
>>> Item.query.all()

?Start the db up again
>>> python
>>> from server import app, db | from market.models import db
>>> app.app_context().push()
>>> db.create_all()
>>> from server import Item

?clear terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')
 -->
