import sqlite3
import os
# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear la tabla 'usuarios'
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')

# Insertar un usuario de prueba
cursor.execute(
    "INSERT OR IGNORE INTO usuarios (username, password) VALUES (?, ?)", ('admin', '1234'))

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("✅ Base de datos creada con el usuario admin / 1234")
