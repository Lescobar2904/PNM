# Plataforma EBB – Gestión de Empresas para Contadores

EBB es una aplicación web desarrollada en Flask que permite a contadores registrar múltiples empresas, visualizar sus datos y gestionar sus facturas. El sistema está enfocado en facilitar la administración de información contable por empresa.

---

## 🚀 Funcionalidades actuales

- ✅ Registro de usuarios con correo y contraseña
- ✅ Inicio de sesión con validación
- ✅ Dashboard personalizado por usuario
- ✅ Crear empresas asociadas al usuario activo
- ✅ Visualizar listado de empresas propias
- ✅ Subir archivos de facturas por empresa (PDF o imagen)
- ✅ Ver facturas asociadas a cada empresa
- ✅ Navegación segura mediante sesión (`session`)
- ✅ Estilo visual limpio y minimalista
- ✅ Mensajes de retroalimentación (`flash`)

---

## 🧪 Datos de prueba

Puedes probar la app con los siguientes pasos:

1. Inicia desde [https://pnm.onrender.com](https://pnm.onrender.com)
2. Ve a **Crear cuenta**
3. Registra un usuario con un correo único
4. Accede al dashboard
5. Crea una empresa (ej. “Contabilidad Uno”)
6. Sube una factura PDF de ejemplo
7. Visualiza el listado de facturas

---

## 🛠 Cómo ejecutar el proyecto localmente

1. Clona este repositorio:

   ```bash
   git clone https://github.com/TUUSUARIO/PNM
   cd PNM
(Opcional) Crea y activa un entorno virtual:

bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate  # en Windows
Instala las dependencias necesarias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta el servidor local:

bash
Copiar
Editar
python run.py
Abre tu navegador en http://localhost:5000

🧩 Tecnologías utilizadas
Python 3.11

Flask

Jinja2 (plantillas)

SQLAlchemy + SQLite

HTML/CSS minimalista

Render (para despliegue)