import sqlite3

conn = sqlite3.connect('database.db') # Estabelece conecção com o banco de dados

cursor = conn.cursor() # Cria um cursor para interagir com a tabela

def create_table(user): # Função que vai criar uma tabela
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {user} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user INTEGER NOT NULL,
        name TEXT NOT NULL,
        price REAL NOT NULL
)''')

create_table("paulo")