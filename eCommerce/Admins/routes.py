from eCommerce import db
from flask import Blueprint,render_template, redirect, request, url_for, flash
from eCommerce.models import Product, Admin
from eCommerce.Admins.forms import AddProductForm
from eCommerce.common_froms import SearchForm
from eCommerce.Admins.utils import renameAndSave

admins = Blueprint('admins', __name__)

@admins.route("/admin/search/<string:search_term>")
def adminSearch(search_term):
    
    page = request.args.get('page',1,type=int)
    paginated_searched_items = Product.query.filter( Product.name.contains(search_term) ).paginate(page=page, per_page=10)

    return render_template('admin_searched_items.html', title='Searched Items', paginated_searched_items=paginated_searched_items, search_term=search_term)


@admins.route("/admin", methods=['GET', 'POST'])
def home():

    admin = Admin.query.first() # Demo current_admin
    
    form = SearchForm()
    if form.validate_on_submit():
        
        return redirect(url_for('admins.adminSearch', search_term=form.search_term.data))


    return render_template('admin_home.html', admin=admin, form=form)

@admins.route("/admin/add", methods=['GET', 'POST'])
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


@admins.route("/admin/product/<int:id>", methods=['GET', 'POST'])
def updateProduct(id):
    
    return render_template('update_product.html', title='Update Product', id=id)