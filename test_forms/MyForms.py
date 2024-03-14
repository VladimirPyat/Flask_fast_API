from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class FillForm(FlaskForm):
    def __init__(self, n=1):
        super(FillForm, self).__init__()
        self.n = n
        for i in range(self.n):
            setattr(FillForm, f'name_{i}', StringField(f'Name {i}', validators=[DataRequired()]))
            setattr(FillForm, f'grade_{i}', IntegerField(f'Grade {i}', validators=[DataRequired()]))

