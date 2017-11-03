from app import create_app
from flask_sqlalchemy import SQLAlchemy

app = create_app()
# Setup the database.
db = SQLAlchemy(app)

class Executives(db.Model):
    EID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    interest = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<Executives %r>' % self.name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)