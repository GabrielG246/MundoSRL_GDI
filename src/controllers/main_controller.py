import sqlite3
import os

dir_actual= os.path.dirname(os.path.abspath(__file__))
dir_bd= os.path.join(dir_actual, '..', '..', 'db', 'mundo_srl.db')

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
        proveedor_id INTEGER,
        materia_nombre TEXT NOT NULL,
        materia_medida TEXT,
        materia_descripcion TEXT,
        materia_precio REAL DEFAULT 0,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id),
        FOREIGN KEY (proveedor_id) REFERENCES proveedor_cliente(id)
        )
    ''')

    #Tabla Proveedor_Cliente
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS proveedor_cliente (
        id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        PC_nombre TEXT,
        PC_email TEXT,
        PC_telefono INTEGER
        )
    ''')

    #Tabla Servicios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS servicios (
        id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        proveedor_id INTEGER,
        categoria_id INTEGER,
        servicio_nombre TEXT NOT NULL UNIQUE,
        servicio_descripcion TEXT,
        servicio_precio REAL DEFAULT 0,
        FOREIGN KEY (proveedor_id) REFERENCES proveedor_cliente(id),
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    ''')

    #Tabla de Productos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        categoria_id INTEGER,
        producto_nombre TEXT NOT NULL,
        producto_descripcion TEXT,
        producto_stock REAL DEFAULT 0,
        producto_precio REAL DEFAULT 0,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    ''')

    #Tabla de Movimientos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movimientos (
        id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        producto_id INTEGER,
        materia_id INTEGER,
        cliente_id INTEGER,
        movimiento_fecha TEXT,
        movimiento_cantidad REAL NOT NULL,
        FOREIGN KEY (producto_id) REFERENCES productos(id),
        FOREIGN KEY (materia_id) REFERENCES materia_prima(id),
        FOREIGN KEY (cliente_id) REFERENCES proveedor_cliente(id)
        )
    ''')

    #Tabla de Produccion
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produccion (
        id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        materia_id INTEGER,
        servicio_id INTEGER,
        cantidad_materia REAL DEFAULT 0,
        cantidad_servicio REAL DEFAULT 0,
        FOREIGN KEY (materia_id) REFERENCES materia_prima(id),
        FOREIGN KEY (servicio_id) REFERENCES servicios(id)
        )
    ''')



    print('Tablas Creadas')
    cursor.close()
    conn.close()



