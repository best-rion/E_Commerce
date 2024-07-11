from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed
from wtforms import IntegerField, StringField, FloatField, SubmitField
  
class AddProductForm(FlaskForm):  
   name = StringField("Product Name", validators=[DataRequired()
                                                ,Length(max=20)])
   price = FloatField("Product Price",  validators=[DataRequired()])

   stock = IntegerField("Quantity",  validators=[DataRequired()])
   picture = FileField("Insert Image", validators=[FileAllowed( ['jpg', 'png'] )])
   submit = SubmitField("Submit")