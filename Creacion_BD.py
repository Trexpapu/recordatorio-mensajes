import sqlite3 as sql

# Conexión a la base de datos
conexion = sql.connect("USUARIOS_WP.db")
cursor = conexion.cursor()

# Crear tabla de usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS USUARIOS (
    USUARIO_ID INTEGER PRIMARY KEY,
    NOMBRE TEXT,
    CELULAR TEXT
)
""")

# Crear tabla de mensajes con columna 'FECHA'
cursor.execute("""
CREATE TABLE IF NOT EXISTS MENSAJES (
    MENSAJE_ID INTEGER PRIMARY KEY,
    USUARIO_ID INTEGER,
    FECHA DATE,
    MENSAJE TEXT,
    FOREIGN KEY (USUARIO_ID) REFERENCES USUARIOS (USUARIO_ID)
)
""")

# Guardar los cambios
conexion.commit()

print("Tablas creadas correctamente")
conexion.close()