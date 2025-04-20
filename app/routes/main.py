from flask import Blueprint, render_template, redirect, url_for, request

main_bp = Blueprint('main', __name__)

# Simulación de datos de empresas (en lugar de base de datos)
empresas_data = {
    "1": {"nombre": "Inversiones López SpA", "rut": "76.543.210-9"},
    "2": {"nombre": "Distribuidora Eléctrica Ltda.", "rut": "77.123.456-1"},
}

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')
        return redirect(url_for('main.dashboard'))  # Acceso directo sin validar
    return render_template('login.html')

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', empresas=empresas_data)

@main_bp.route('/nueva-empresa', methods=['POST'])
def nueva_empresa():
    nombre = request.form.get('nombre')
    rut = request.form.get('rut')
    nueva_id = str(len(empresas_data) + 1)
    empresas_data[nueva_id] = {"nombre": nombre, "rut": rut}
    print(f"Empresa agregada: {nombre} - {rut}")
    return redirect(url_for('main.dashboard'))

@main_bp.route('/empresa/<empresa_id>')
def ver_empresa(empresa_id):
    empresa = empresas_data.get(empresa_id)
    if not empresa:
        return "Empresa no encontrada", 404
    return render_template('empresa.html', empresa=empresa, empresa_id=empresa_id)

@main_bp.route('/empresa/<empresa_id>/subir', methods=['POST'])
def subir_factura_empresa(empresa_id):
    empresa = empresas_data.get(empresa_id)
    if not empresa:
        return "Empresa no encontrada", 404
    archivo = request.files.get("factura_pdf")
    if archivo:
        print(f"Factura subida para empresa {empresa['nombre']}: {archivo.filename}")
        # Aquí podrías guardar el archivo en /uploads si lo deseas
    return redirect(url_for('main.ver_empresa', empresa_id=empresa_id))

@main_bp.route('/upload')
def upload():
    return render_template('upload.html')

@main_bp.route('/profile')
def profile():
    return render_template('profile.html')
