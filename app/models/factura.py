from app import db

class Factura(db.Model):
    __tablename__ = 'factura'

    id = db.Column(db.Integer, primary_key=True)
    archivo_nombre = db.Column(db.String(120))  # opcional
    nombre_manual = db.Column(db.String(100))
    fecha = db.Column(db.String(20))  # puedes usar Date si lo prefieres
    monto = db.Column(db.Float)
    descripcion = db.Column(db.String(255))
    
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
