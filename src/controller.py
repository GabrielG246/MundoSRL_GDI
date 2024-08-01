import sqlite3
import os

dir_actual= os.path.dirname(os.path.abspath(__file__))
dir_bd= os.path.join(dir_actual, '..', 'db', 'mundo_srl.db')

#Crear Base de Datos
def CrearBD():
    conn= sqlite3.connect(dir_bd)


def CrearTablas():
    conn= sqlite3.connect(dir_bd)
    cursor= conn.cursor()

    #Tabla Categorias
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        categoria_nombre TEXT NOT NULL UNIQUE,
        categoria_aumento INTEGER DEFAULT 0
        )
    ''')

    #Tabla Materia_Prima
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS materia_prima (
        id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        categoria_id INTEGER,
        materia_nombre TEXT NOT NULL,
        materia_medida TEXT,
        materia_descripcion TEXT,
        materia_precio INTEGER DEFAULT 0,
        FOREIGN KEY (id_categoria) REFERENCES categorias(id)
        )
    ''')
    cursor.close()
    conn.close()



