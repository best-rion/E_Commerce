from eCommerce.models import Product
from eCommerce import app, db

with app.app_context():
    product1 = Product(name='Titan R-1320', price=701, stock=7)
    db.session.add(product1)
    db.session.commit()
