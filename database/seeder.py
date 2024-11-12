import sqlite3 as sql


DB_PATH = "C:\\Users\\luisd\\OneDrive\\Escritorio\\Programación\\Proyecto PAS (Pagina web)\\ApiPAS\\database\\barbershop.db"


def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE barbers (
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
        ("Luis Vergara", "Corte", 10000),
        ("Juan Salgado", "Barba", 6000),
        ("Angel Mendoza", "Cejas", 4000)
    ]
    cursor.executemany("""INSERT INTO barbers VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    addValues()