from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField
from wtforms import IntegerField, StringField, FloatField, SubmitField
  
class AddProductForm(FlaskForm):  
   name = StringField("Product Name", validators=[DataRequired("Please enter product name.")
                                                ,Length(max=20)])
   price = FloatField("Product Price",  validators=[DataRequired("Please enter product price.")])

   stock = IntegerField("Quantity",  validators=[DataRequired("How many?. Enter 0 if zero.")])
   picture = FileField("Insert Image")
   submit = SubmitField("Submit")