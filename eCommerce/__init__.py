from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from eCommerce.froms import AddProductForm
import os

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eCommerce.db'
db.init_app(app)

app.config['SECRET_KEY'] = os.urandom(32)

from eCommerce.models import Product

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():

    products = Product.query.all()
    return render_template('about.html', title='About', products=products)

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AddProductForm()

    if form.validate_on_submit():
        new_product = Product(name=form.name.data, price=form.price.data)
        if form.stock.data:
            new_product.stock = form.stock.data
        #if form.picture.data != Null:
        #    new_product.stock = form.stock.data
        db.session.add(new_product)
        db.session.commit()
        form.name.data = ''
        form.price.data = ''
        form.stock.data = ''

    return render_template('add_product.html', title='Admin', form=form)
    