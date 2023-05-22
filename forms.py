from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Add Pet Form"""
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Comments", validators=[Optional(), Length(min=1)])


class EditPetForm(FlaskForm):
    """Edit Pet Form"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Comments", validators=[Optional(), Length(min=1)])
    available = BooleanField("Available?")