from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # 🔐 Clave secreta para manejo de sesiones y flash
    app.secret_key = 'clave-super-secreta-123'  # cámbiala en producción

    # ⚙️ Configuración de la base de datos SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ebb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos
    db.init_app(app)

    # Registrar el blueprint principal
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    # Crear tablas si no existen
    with app.app_context():
        from app.models import Empresa, Factura, Usuario  # importa todos tus modelos
        db.create_all()

    return app
