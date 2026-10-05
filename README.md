# 🛒 Ferretería "El Tornillo Dorado" - Proyecto Integrador Final

**Universidad Estatal Amazónica (UEA)**  
**Carrera:** Tecnologías de la Información  
**Asignatura:** Desarrollo de Aplicaciones Web (2626-UEA-L-UFPTI-004-D)  
**Estudiante:** Clara Anahí González Apolo  
**Repositorio GitHub:** [https://github.com/anis1605/2626---DESARROLLO-DE-APLICACIONES-WEB----UEA-L-UFPTI-004](https://github.com/anis1605/2626---DESARROLLO-DE-APLICACIONES-WEB----UEA-L-UFPTI-004)  
**Despliegue Frontend (GitHub Pages):** [https://anis1605.github.io/2626---DESARROLLO-DE-APLICACIONES-WEB----UEA-L-UFPTI-004/](https://anis1605.github.io/2626---DESARROLLO-DE-APLICACIONES-WEB----UEA-L-UFPTI-004/)  

---

## 📌 Descripción del Proyecto

Aplicación web completa desarrollada con el microframework **Flask**, integrada con una base de datos relacional **PostgreSQL**, que implementa:
1. **Sistema de Autenticación y Control de Acceso:** Registro de usuarios con hashing seguro de contraseñas (`Werkzeug` con algoritmo `scrypt`), inicio de sesión, sesiones seguras mediante `Flask-Login`, protección estricta de rutas privadas con `@login_required` y cierre seguro de sesión (`logout_user`).
2. **Operaciones CRUD Completas:** Crear, Leer, Actualizar y Eliminar registros en todos los módulos de gestión empresarial (Productos, Proveedores, Clientes y Facturación).
3. **Base de Datos Relacional con Múltiples Tablas y Claves Foráneas:** 5 tablas normalizadas (`usuarios`, `proveedores`, `productos`, `clientes`, `facturas`) con integridad referencial (`PRIMARY KEY`, `FOREIGN KEY`, `ON DELETE SET NULL`, `ON UPDATE CASCADE`) y consultas multi-tabla con `JOIN`.
4. **Diseño de Interfaz Profesional:** Estética pastel moderna, layout responsivo con Bootstrap 5, validaciones de formulario con Flask-WTF y protección CSRF.

---

## 🏗️ Arquitectura y Estructura del Proyecto

```text
Proyecto_Integrador/
│
├── app.py                      # Controlador principal, rutas y lógica de autenticación y CRUD
├── models.py                   # Entidad Usuario (UserMixin) y métodos de acceso a datos
├── requirements.txt            # Dependencias del proyecto (Flask, psycopg2, Flask-Login, etc.)
├── Procfile                    # Configuración de inicio para despliegue en Render (gunicorn)
├── README.md                   # Documentación técnica completa
├── test_app.py                 # Suite de pruebas automatizadas con pytest
│
├── conexion/                   # Módulo de conexión a base de datos
│   ├── __init__.py
│   └── conexion.py             # Conector psycopg2 para PostgreSQL con soporte local y nube
│
├── sql/                        # Scripts DDL de base de datos
│   └── esquema.sql             # Esquema DDL con 5 tablas y datos iniciales de prueba
│
├── forms/                      # Formularios validados con Flask-WTF y WTForms
│   ├── __init__.py
│   ├── login_form.py           # Formulario de inicio de sesión
│   ├── usuario_form.py         # Formulario de registro de usuarios
│   ├── producto_form.py        # Formulario de creación y edición de productos
│   ├── cliente_form.py         # Formulario de clientes
│   ├── proveedor_form.py       # Formulario de proveedores
│   └── facturacion_form.py     # Formulario de emisión de facturas
│
├── templates/                  # Plantillas Jinja2 renderizadas dinámicamente
│   ├── base.html               # Plantilla maestra con diseño pastel y Navbar dinámico
│   ├── index.html              # Página principal informativa
│   ├── login.html              # Vista de autenticación
│   ├── registro.html           # Vista de registro de nuevos usuarios
│   ├── dashboard.html          # Panel de control administrativo
│   ├── productos.html          # Listado y gestión de productos (CRUD)
│   ├── formulario_producto.html# Formulario para agregar/editar productos
│   ├── clientes.html           # Listado y gestión de clientes (CRUD)
│   ├── formulario_cliente.html # Formulario para clientes
│   ├── proveedores.html        # Listado y gestión de proveedores (CRUD)
│   ├── formulario_proveedor.html # Formulario para proveedores
│   ├── facturacion.html        # Listado de facturas emitidas con JOIN a clientes
│   ├── formulario_facturacion.html # Formulario de nueva factura
│   └── components/
│       ├── navbar.html         # Barra de navegación reutilizable
│       └── footer.html         # Pie de página institucional
│
└── static/                     # Archivos estáticos
    ├── css/style.css           # Hoja de estilos con paleta pastel y microinteracciones
    └── js/script.js            # Lógica interactiva del cliente
```

---

## 🗄️ Esquema de la Base de Datos (PostgreSQL)

El sistema cuenta con 5 tablas interconectadas:

1. **`usuarios`**: Almacena los usuarios autorizados. Las contraseñas están protegidas mediante hash scrypt.
2. **`proveedores`**: Catálogo de proveedores identificados por su RUC (Clave Primaria).
3. **`productos`**: Inventario de materiales con clave foránea `proveedor_ruc` hacia `proveedores(ruc)`.
4. **`clientes`**: Registro de clientes con identificación RUC/Cédula (Clave Primaria).
5. **`facturas`**: Registro de ventas con clave foránea `cliente_ruc` hacia `clientes(ruc)`.

### Consulta con JOIN Implementada:
```sql
SELECT p.id, p.nombre, p.categoria, p.unidad, p.stock, p.precio, p.proveedor_ruc,
       pr.empresa AS proveedor_empresa
FROM productos p
LEFT JOIN proveedores pr ON p.proveedor_ruc = pr.ruc
ORDER BY p.nombre ASC;
```

---

## 🚀 Instalación y Ejecución Local

### 1. Clonar el repositorio:
```bash
git clone https://github.com/anis1605/2626---DESARROLLO-DE-APLICACIONES-WEB----UEA-L-UFPTI-004.git
cd 2626---DESARROLLO-DE-APLICACIONES-WEB----UEA-L-UFPTI-004
```

### 2. Crear y activar el entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate   # En Windows
```

### 3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno y base de datos:
Configurar en archivo `.env` o en el sistema:
```bash
export DB_HOST=localhost
export DB_USER=postgres
export DB_PASSWORD=tu_password
export DB_NAME=ferreteria_db
export DB_PORT=5432
export SECRET_KEY=clave_secreta_super_segura
```
*(Opcionalmente definir `DATABASE_URL=postgresql://user:password@host:port/dbname`)*

### 5. Ejecutar la aplicación:
```bash
python app.py
```
Abrir en el navegador: `http://localhost:5000`

---

## 👤 Credenciales Iniciales de Prueba

- **Usuario:** `admin` | **Contraseña:** `admin123`
- **Usuario:** `anis`  | **Contraseña:** `anis2026`

---

## ☁️ Despliegue en Render

El repositorio incluye el archivo `Procfile` y la compatibilidad completa con variables de entorno para Render:
1. Conectar el repositorio de GitHub en Render.
2. Seleccionar servicio **Web Service** (Python).
3. **Build Command:** `pip install -r requirements.txt`
4. **Start Command:** `gunicorn app:app`
5. En Environment Variables, agregar:
   - `DATABASE_URL`: URL de la base de datos PostgreSQL de Render.
   - `SECRET_KEY`: Cadena secreta segura para sesiones.
   - `PYTHON_VERSION`: `3.12.3`
