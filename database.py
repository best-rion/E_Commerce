from models import Product
from eCommerce import app

with app.app_context():
    product1=Product.query.first()
print(product1.quantity)

