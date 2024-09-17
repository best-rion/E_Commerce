from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eCommerce.db'
app.config['SECRET_KEY'] = os.urandom(32)
db = SQLAlchemy()
db.init_app(app)

from eCommerce.Users.routes import users
from eCommerce.Admins.routes import admins
from eCommerce.Carts.routes import carts


app.register_blueprint(users)
app.register_blueprint(admins)
app.register_blueprint(carts)



