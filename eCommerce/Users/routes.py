from flask import Blueprint,render_template, redirect, request, url_for, flash
from eCommerce.models import Product
from eCommerce.common_froms import SearchForm
import json


users = Blueprint('users', __name__,
                  template_folder='templates')


class UserClass:

    default_quantity = 1

    def __init__(self):
        self.cart=[]
        self.quantity_list = []
        self.numberOfItems = 0

    def addItemToCart(self, product_id):

        if product_id not in self.cart:

            self.cart.append(product_id)
            self.quantity_list.append(UserClass.default_quantity)
            self.numberOfItems += 1 #one product was added

    def updateCart(self, index, sign):


        if sign == "+":
            self.quantity_list[index] += 1
            self.numberOfItems += 1 #one product was added

        if sign == "-":

            if self.quantity_list[index] > 0:
                self.quantity_list[index] -=1

                self.numberOfItems -= 1 #one product was removed
        for index,product in enumerate(self.cart):
            print(str(product)+'\t'+str(self.quantity_list[index])+'\n')


    def deleteFromCart(self, index):
            
        self.cart.pop(index)
        self.numberOfItems -= self.quantity_list[index]
        self.quantity_list.pop(index)


test_user = UserClass()


@users.route("/search/<string:search_term>", methods=['GET', 'POST'])
def userSearch(search_term):
    
    page = request.args.get('page',1,type=int)
    paginated_products = Product.query.filter(Product.name.contains(search_term)).filter(Product.stock>0).order_by(Product.id.desc()).paginate(page=page, per_page=20)

    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('users.userSearch', search_term=form.search_term.data,  numberOfItems=test_user.numberOfItems))
    
    items_in_cart = test_user.cart

    return render_template('user_searched_items.html', title='Searched Items', form=form,
                            paginated_products=paginated_products, search_term=search_term, numberOfItems=test_user.numberOfItems, items_in_cart=items_in_cart)




@users.route("/", methods=['GET', 'POST'])
def home():
    # Search bar
    page = request.args.get('page', 1, type=int)
    paginated_products = Product.query.filter(Product.stock>0).order_by(Product.id.desc()).paginate(page=page, per_page=20)

    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('users.userSearch', search_term=form.search_term.data,  numberOfItems=test_user.numberOfItems))
    

    items_in_cart = test_user.cart
    
    return render_template('home.html', paginated_products=paginated_products, form=form,   numberOfItems=test_user.numberOfItems, items_in_cart=items_in_cart)

@users.route("/about")
def about():
    return render_template('about.html', title='About')

@users.route("/addToCart", methods=['POST'])
def addToCart():
    global test_user

    product_id = request.form['product_id'] # 'product_id' corresponds to the name inside <input name='product_id'  ......>

    test_user.addItemToCart(product_id=product_id)

    return "Added to cart successfully"


@users.route("/cart", methods=['Get', 'POST'])
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


@users.route("/actionInCart/<int:index>/<string:sign>", methods=['POST'])
def actionInCart(index, sign):
    global test_user


    index = index-1


    test_user.updateCart(index=index, sign=sign)


    return redirect(url_for('users.cart'))


@users.route("/deleteInCart", methods=['POST'])
def deleteInCart():
    
    index= request.args.get('index',0, type=int )-1

    global test_user


    test_user.deleteFromCart(index=index)

    return redirect(url_for('users.cart'))



@users.route("/pay", methods=['GET'])
def pay():
    return render_template('pay.html')
    