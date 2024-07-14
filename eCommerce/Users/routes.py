from flask import Blueprint,render_template, redirect, request, url_for
from eCommerce.models import Product
from eCommerce.common_froms import SearchForm


users = Blueprint('users', __name__,
                  template_folder='templates')


@users.route("/search/<string:search_term>", methods=['GET', 'POST'])
def userSearch(search_term):
    
    page = request.args.get('page',1,type=int)
    paginated_searched_items = Product.query.filter(Product.name.contains(search_term)).filter(Product.stock>0).order_by(Product.id.desc()).paginate(page=page, per_page=20)

    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('users.userSearch', search_term=form.search_term.data))

    return render_template('user_searched_items.html', title='Searched Items', form=form,
                            paginated_searched_items=paginated_searched_items, search_term=search_term)




@users.route("/", methods=['GET', 'POST'])
def home():
    # Search bar

    page = request.args.get('page', 1, type=int)
    paginated_products = Product.query.filter(Product.stock>0).order_by(Product.id.desc()).paginate(page=page, per_page=20)

    form = SearchForm()
    if form.validate_on_submit():
        
        return redirect(url_for('users.userSearch', search_term=form.search_term.data))
    
    return render_template('home.html', paginated_products=paginated_products, form=form)

@users.route("/about")
def about():
    return render_template('about.html', title='About')