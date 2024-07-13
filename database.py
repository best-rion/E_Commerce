from eCommerce.models import Product
from eCommerce import app, db
import json

with open("watches.json", "r") as json_file:
    json_dictionary = json.load(json_file)

watches = json_dictionary["list"]

with app.app_context():
    for watch in watches:
        product = Product(name=watch["name"], price=watch["price"], stock=watch["stock"])
        db.session.add(product)
    
    db.session.commit()
