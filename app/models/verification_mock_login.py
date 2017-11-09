from wtforms import Form, StringField, PasswordField, validators

class VerificationMockForm(Form):
    username = StringField('Lifetime ID', [validators.DataRequired()])
    password = PasswordField('Password')