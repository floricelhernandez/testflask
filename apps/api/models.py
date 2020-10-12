from apps import db
from sqlalchemy.orm import relationship

class Tienda(db.Model):
    __tablename__ = 'tienda'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    direccion = db.Column(db.String())
    stock = db.relationship("Stock")

    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def __repr__(self):
        return '{}'.format(self.nombre)

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'direccion': self.direccion
        }

class Producto (db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '{}'.format(self.nombre)

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }

class Stock(db.Model):
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    tienda_id = db.Column(db.Integer, db.ForeignKey('tienda.id'))
    tienda = db.relationship('Tienda', back_populates='stock')
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    producto = db.relationship('Producto')
    existencia = db.Column(db.Integer)

    def __init__(self, producto_id, existencia):
        self.producto_id = producto_id
        self.existencia = existencia
    
    def __repr__(self):
        return '{}'.format(self.existencia)

    def serialize(self):
        return {
            'id': self.id,
            'tienda': self.tienda.serialize(),
            'producto': self.producto.serialize(),
            'existencia': self.existencia
        }
