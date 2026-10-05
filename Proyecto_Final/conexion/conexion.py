import os
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

# Parámetros de configuración de la base de datos relacional PostgreSQL
DATABASE_URL = os.environ.get('DATABASE_URL')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')
DB_NAME = os.environ.get('DB_NAME', 'ferreteria_db')
DB_PORT = os.environ.get('DB_PORT', '5432')

def obtener_conexion():
    """
    Establece y retorna una conexión activa al servidor PostgreSQL.
    """
    try:
        if DATABASE_URL:
            conexion = psycopg2.connect(DATABASE_URL)
        else:
            conexion = psycopg2.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                dbname=DB_NAME,
                port=DB_PORT
            )
        return conexion
    except OperationalError as e:
        print(f"[ERROR CONEXION POSTGRESQL]: No se pudo conectar a la base de datos: {e}")
        raise e

def inicializar_base_datos():
    """
    Ejecuta el script DDL sql/esquema.sql en caso de que las tablas no existan previamente.
    (La base de datos ya debe estar creada o provisionada en Render)
    """
    try:
        # En PostgreSQL, si es local, intentamos asegurar que exista la BD conectándonos a postgres
        if not DATABASE_URL:
            try:
                conn_server = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname='postgres', port=DB_PORT)
                conn_server.autocommit = True
                cursor = conn_server.cursor()
                cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{DB_NAME}'")
                exists = cursor.fetchone()
                if not exists:
                    cursor.execute(f"CREATE DATABASE {DB_NAME}")
                cursor.close()
                conn_server.close()
            except Exception as e:
                print(f"[ADVERTENCIA]: No se pudo verificar o crear la BD automáticamente: {e}")

        # Conectar a la base de datos y ejecutar esquema.sql
        ruta_esquema = os.path.join(os.path.dirname(__file__), '..', 'sql', 'esquema.sql')
        if os.path.exists(ruta_esquema):
            conn_db = obtener_conexion()
            cursor_db = conn_db.cursor()

            with open(ruta_esquema, 'r', encoding='utf-8') as f:
                sql_content = f.read()

            # En psycopg2 se puede ejecutar todo el script de golpe
            cursor_db.execute(sql_content)
            conn_db.commit()
            cursor_db.close()
            conn_db.close()
            print(f"[INFO POSTGRESQL]: Esquema inicializado y sincronizado correctamente.")

    except Exception as e:
        print(f"[ADVERTENCIA POSTGRESQL]: Error durante la verificación inicial del esquema: {e}")
