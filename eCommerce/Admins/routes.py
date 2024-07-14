from eCommerce import db, app
from flask import Blueprint,render_template, redirect, request, url_for, flash
from eCommerce.models import Product, Admin
from eCommerce.Admins.forms import AddProductForm, UpdateProductForm
from eCommerce.common_froms import SearchForm
from eCommerce.Admins.utils import renameAndSave
import os

admins = Blueprint('admins', __name__, template_folder='templates')


search_term_before_edit=''
page_before_edit=0


@admins.route("/admin/search/<string:search_term>")
def adminSearch(search_term):
    
    page = request.args.get('page',1,type=int)
    paginated_searched_items = Product.query.filter( Product.name.contains(search_term) ).order_by(Product.id.desc()).paginate(page=page, per_page=10)

    global page_before_edit
    global search_term_before_edit
    page_before_edit = page
    search_term_before_edit = search_term

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
                            , detail = form.detail.data
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

    product = Product.query.get(id)

    form = UpdateProductForm(product.detail)

    if form.validate_on_submit():

        
        product.name = form.name.data
        product.detail = form.detail.data
        product.price = form.price.data
        product.stock = form.stock.data

        if form.picture.data:

            # Deleting old picture
            picture_name = product.picture

            if picture_name != 'default.jpg':
                os.remove(os.path.join(app.root_path, 'static','images' , picture_name ))

            # Deleted old picture

            product.picture = renameAndSave(form.picture.data)


        db.session.commit()

        flash(f"The product with ID {product.id} has been Updated", 'success')

        return redirect(url_for('admins.home')+f'/search/{search_term_before_edit}?page={page_before_edit}')

    elif request.method == 'GET':

        form.name.data = product.name
        form.detail.data = product.detail
        form.price.data = product.price
        form.stock.data = product.stock
    
    return render_template('update_product.html', title='Update Product', product=product, form=form)



@admins.route("/admin/product/<int:id>/delete", methods=['POST'])
def deleteProduct(id):

    product = Product.query.get_or_404(id)

    # Deleting image
    picture_name = product.picture

    if picture_name != 'default.jpg':
        os.remove(os.path.join(app.root_path, 'static','images' , picture_name )) 

    db.session.delete(product)
    db.session.commit()

    flash(f'Product with ID {id} has been deleted successfully', 'success')

    return redirect(url_for('admins.home')+f'/search/{search_term_before_edit}?page={page_before_edit}')
