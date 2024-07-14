from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):  
   search_term = StringField("Search by name", validators=[DataRequired(),Length(max=20)])
   submit = SubmitField("Submit")
