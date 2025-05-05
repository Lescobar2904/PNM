from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app import db
from app.models import Empresa, Factura, Usuario

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        existente = Usuario.query.filter_by(correo=correo).first()
        if existente:
            flash('El correo ya está registrado.')
            return redirect(url_for('main.registro'))

        nuevo = Usuario(nombre=nombre, correo=correo)
        nuevo.set_password(contrasena)
        db.session.add(nuevo)
        db.session.commit()
        flash('Cuenta creada correctamente. Ahora puedes ingresar.')
        return redirect(url_for('main.login'))

    return render_template('registro.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        usuario = Usuario.query.filter_by(correo=correo).first()
        if usuario and usuario.check_password(contrasena):
            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.nombre
            session['usuario_correo'] = usuario.correo
            return redirect(url_for('main.dashboard'))
        else:
            flash('Correo o contraseña incorrectos.')
            return redirect(url_for('main.login'))

    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@main_bp.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión primero.')
        return redirect(url_for('main.login'))

    usuario_id = session['usuario_id']
    empresas = Empresa.query.filter_by(usuario_id=usuario_id).all()
    return render_template('dashboard.html', empresas=empresas)


@main_bp.route('/nueva-empresa', methods=['POST'])
def nueva_empresa():
    if 'usuario_id' not in session:
        return redirect(url_for('main.login'))

    nombre = request.form.get('nombre')
    rut = request.form.get('rut')
    usuario_id = session['usuario_id']

    nueva = Empresa(nombre=nombre, rut=rut, usuario_id=usuario_id)
    db.session.add(nueva)
    db.session.commit()
    return redirect(url_for('main.dashboard'))


@main_bp.route('/empresa/<int:empresa_id>')
def ver_empresa(empresa_id):
    if 'usuario_id' not in session:
        return redirect(url_for('main.login'))

    empresa = Empresa.query.get_or_404(empresa_id)
    return render_template('empresa.html', empresa=empresa)

@main_bp.route('/empresa/<int:empresa_id>/subir', methods=['POST'])
def subir_factura_empresa(empresa_id):
    if 'usuario_id' not in session:
        return redirect(url_for('main.login'))

    empresa = Empresa.query.get_or_404(empresa_id)
    archivo = request.files.get("factura_pdf")
    if archivo:
        factura = Factura(archivo_nombre=archivo.filename, empresa_id=empresa.id)
        db.session.add(factura)
        db.session.commit()
    return redirect(url_for('main.ver_empresa', empresa_id=empresa.id))

@main_bp.route('/profile')
def profile():
    if 'usuario_id' not in session:
        return redirect(url_for('main.login'))

    return render_template('profile.html', nombre=session['usuario_nombre'], correo=session['usuario_correo'])
@main_bp.route('/empresa/<int:empresa_id>/factura/manual', methods=['POST'])
def agregar_factura_manual(empresa_id):
    if 'usuario_id' not in session:
        return redirect(url_for('main.login'))

    empresa = Empresa.query.get_or_404(empresa_id)

    if empresa.usuario_id != session['usuario_id']:
        flash("No puedes modificar esta empresa.")
        return redirect(url_for('main.dashboard'))

    nombre = request.form.get('nombre_manual')
    fecha = request.form.get('fecha')
    monto = request.form.get('monto')
    descripcion = request.form.get('descripcion')

    factura = Factura(
        nombre_manual=nombre,
        fecha=fecha,
        monto=monto,
        descripcion=descripcion,
        empresa_id=empresa.id
    )

    db.session.add(factura)
    db.session.commit()
    flash("Factura agregada manualmente.")
    return redirect(url_for('main.ver_empresa', empresa_id=empresa.id))
