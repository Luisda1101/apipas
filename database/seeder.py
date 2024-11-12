<<<<<<< HEAD
import sqlite3 as sql


DB_PATH = "C:\\Users\\luisd\\OneDrive\\Escritorio\\Programación\\Proyecto PAS (Pagina web)\\ApiPAS\\database\\barbershop.db"


def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE streamers (
        name String,
        service String,
        service_value float
    )""")
    conn.commit()
    conn.close()


def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        ("alexelcapo", 10000, 800000),
        ("ibai", 25000, 7000000),
        ("elxokas", 10000, 1000000),
        ("auronplay", 20000, 8000000),
        ("cristinini", 5500, 3000000)
    ]
    cursor.executemany("""INSERT INTO streamers VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
=======
import sqlite3 as sql


DB_PATH = "C:\\Users\\luisd\\OneDrive\\Escritorio\\Programación\\Proyecto PAS (Pagina web)\\ApiPAS\\database\\barbershop.db"


def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE streamers (
        name String,
        service String,
        service_value float
    )""")
    conn.commit()
    conn.close()


def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        ("alexelcapo", 10000, 800000),
        ("ibai", 25000, 7000000),
        ("elxokas", 10000, 1000000),
        ("auronplay", 20000, 8000000),
        ("cristinini", 5500, 3000000)
    ]
    cursor.executemany("""INSERT INTO streamers VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
>>>>>>> 98b0007e253dd00035fa8e5021a15bfba88cc689
    addValues()