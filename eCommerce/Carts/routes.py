from flask import Blueprint, render_template, redirect, url_for, request
from eCommerce.common_froms import SearchForm
from eCommerce.models import Product


carts = Blueprint('carts', __name__, template_folder='templates')



@carts.route("/cart", methods=['Get', 'POST'])
def cart():

    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('users.userSearch', search_term=form.search_term.data,  numberOfItems=test_user.numberOfItems))

    products = []
    total = 0

    for i in range( len(test_user.cart) ):

        product = Product.query.get(test_user.cart[i])
        products.append(product)

        total += product.price * test_user.quantity_list[i]

    return render_template('user_cart.html',  form=form,   numberOfItems=test_user.numberOfItems,
                            products=products, quantity_list=test_user.quantity_list, total=total)


@carts.route("/actionInCart/<int:index>/<string:sign>", methods=['POST'])
def actionInCart(index, sign):
    global test_user


    index = index-1


    test_user.updateCart(index=index, sign=sign)


    return redirect(url_for('users.cart'))


@carts.route("/deleteInCart", methods=['POST'])
def deleteInCart():
    
    index= request.args.get('index',0, type=int )-1

    global test_user


    test_user.deleteFromCart(index=index)

    return redirect(url_for('users.cart'))



@carts.route("/pay", methods=['GET'])
def pay():
    return render_template('pay.html')