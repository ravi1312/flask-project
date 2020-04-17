from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField



class AddOwnerForm(FlaskForm):

    name = StringField('Name Of The Owner')
    pup_id = IntegerField('Id Of The Puppy')
    submit = SubmitField('Add Owner')
