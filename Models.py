<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Barbers(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    service = db.Column(db.String(200))
    service_value = db.Column(db.Float, nullable=False)
    
    def __str__(self):
        return f'Barbero: {self.name} - Servicio: {self.service} - Valor del servicio: {self.service_value}'

    def serialize(self):
        return {
            "rowid": self.rowid,
            "name": self.name,
            "service": self.service,
            "service_value": self.service_value
=======
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Barbers(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    service = db.Column(db.String(200))
    service_value = db.Column(db.Float, nullable=False)
    
    def __str__(self):
        return f'Barbero: {self.name} - Servicio: {self.service} - Valor del servicio: {self.service_value}'

    def serialize(self):
        return {
            "rowid": self.rowid,
            "name": self.name,
            "service": self.service,
            "service_value": self.service_value
>>>>>>> 98b0007e253dd00035fa8e5021a15bfba88cc689
        }