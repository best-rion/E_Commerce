from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired
from eCommerce.models import Product

def validate_unique_detail(form, detail_typed_into_form): # always give form, pore use hobe
   product_with_this_detail = Product.query\
                                    .filter_by(detail=detail_typed_into_form.data)\
                                    .first()
   if product_with_this_detail:
      raise ValidationError("That product is already there.")

  
class AddProductForm(FlaskForm):  
   name = StringField("Product Name", validators=[DataRequired()
                                                ,Length(max=20)])
   detail = StringField("Product Detail", validators=[DataRequired()
                                                ,Length(max=40), validate_unique_detail])
   price = FloatField("Product Price",  validators=[ InputRequired()])

   stock = IntegerField("Quantity",  validators=[ InputRequired()])
   picture = FileField("Insert Image", validators=[FileAllowed( ['jpg', 'png', 'jpeg'] )])
   submit = SubmitField("Submit")
   
   def validate_stock(self, stock):
      if stock.data < 0 :
         raise ValidationError('Quantity must be a positive integer')
      
   def validate_price(self, price):
      if price.data <= 0 :
         raise ValidationError('Quantity must be a positive integer')

   

class UpdateProductForm(FlaskForm):

   def __init__(self, product_detail, *args, **kwargs):
      self.product_detail = product_detail
      super().__init__( *args, **kwargs)

   name = StringField("Product Name", validators=[DataRequired()
                                                ,Length(max=20)])
   detail = StringField("Product Detail", validators=[DataRequired()
                                                ,Length(max=40)])
   price = FloatField("Product Price", validators=[ InputRequired()])

   stock = IntegerField("Quantity", validators=[InputRequired()])
   picture = FileField("Insert Image", validators=[FileAllowed( ['jpg', 'png', 'jpeg'] )])
   submit = SubmitField("Update")


   def validate_detail(self, detail):

      if detail.data != self.product_detail:
         detail = Product.query.filter_by(detail=detail.data).first()
         if detail:
               raise ValidationError('That detail is already there')
         
   def validate_stock(self, stock):
      if stock.data < 0 :
         raise ValidationError('Quantity must be a positive integer')
      
   def validate_price(self, price):
      if price.data <= 0 :
         raise ValidationError('Check price again')