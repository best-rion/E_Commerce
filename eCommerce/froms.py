from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms import IntegerField, StringField, FloatField, SubmitField
from eCommerce.models import Product



def validate_unique_name(form, name_typed_into_form): # always give form, pore use hobe
   product_with_this_name = Product.query\
                                    .filter_by(name=name_typed_into_form.data)\
                                    .first()
   if product_with_this_name:
      raise ValidationError("That product is already there.")

  
class AddProductForm(FlaskForm):  
   name = StringField("Product Name", validators=[DataRequired()
                                                ,Length(max=20), validate_unique_name])
   price = FloatField("Product Price",  validators=[DataRequired()])

   stock = IntegerField("Quantity",  validators=[DataRequired()])
   picture = FileField("Insert Image", validators=[FileAllowed( ['jpg', 'png', 'jpeg'] )])
   submit = SubmitField("Submit")
