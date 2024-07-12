from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from eCommerce.utitlities import renameAndSave
import os

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eCommerce.db'
db.init_app(app)

app.config['SECRET_KEY'] = os.urandom(32)

from eCommerce.models import Product
from eCommerce.froms import AddProductForm

@app.route("/")
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route("/about")
def about():
    return render_template('about.html', title='About')





@app.route("/admin/add", methods=['GET', 'POST'])
def addProduct():

    form = AddProductForm()

    if form.validate_on_submit():
        
        new_product = Product(name = form.name.data
                            , price = form.price.data
                            , stock = form.stock.data
                            )
        if form.picture.data:
            new_product.picture = renameAndSave(form.picture.data)

        db.session.add(new_product)
        db.session.commit()

        form = AddProductForm(formdata=None)
        
    return render_template('add_product.html', title='Add Product', form=form)
    