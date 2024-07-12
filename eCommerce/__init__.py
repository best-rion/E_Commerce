from flask import Flask, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from eCommerce.utitlities import renameAndSave
import os

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eCommerce.db'
db.init_app(app)

app.config['SECRET_KEY'] = os.urandom(32)

from eCommerce.models import Product, Admin
from eCommerce.froms import AddProductForm, SearchForm

@app.route("/")
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/admin/search/<string:search_term>")
def searchItems(search_term):

    items = Product.query.filter( Product.name.contains(search_term) ).all()

    return render_template('searched_items.html', title='Searched Items', items=items, search_term=search_term)


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    # i have to send current admin's name, id, email
    # i have to receive a search query about a product name
    # and send a page of the product with info
    # pagination user e lagabo, aage basic admin banai

    admin = Admin.query.first() # Demo current_admin
    
    form = SearchForm()
    if form.validate_on_submit():
        
        return redirect(url_for('searchItems', search_term=form.search_term.data))


    return render_template('admin_home.html', admin=admin, form=form)

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

        flash("The product has been added", 'success')

        form = AddProductForm(formdata=None)
        
    return render_template('add_product.html', title='Add Product', form=form)


@app.route("/admin/product/<int:id>", methods=['GET', 'POST'])
def updateProduct(id):
    
    return render_template('update_product.html', title='Update Product', id=id)

