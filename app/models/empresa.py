from app import db

class Empresa(db.Model):
    __tablename__ = 'empresa'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rut = db.Column(db.String(20), nullable=False)
    
    # Relación con Usuario
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    # Relación con Facturas
    facturas = db.relationship('Factura', backref='empresa', lazy=True)
