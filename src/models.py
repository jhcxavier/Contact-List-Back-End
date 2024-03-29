from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ContactList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=True)
    address = db.Column(db.String(120), unique=True, nullable=True)

    def __repr__(self):
        return '<Contact %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "id": self.id
            # "address": self.address
        }
