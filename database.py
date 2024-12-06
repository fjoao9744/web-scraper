import sqlite3
import asyncio

conn = sqlite3.connect('database.db') # Estabelece conecção com o banco de dados

cursor = conn.cursor() # Cria um cursor para interagir com a tabela

async def create_table(user): # Função que vai criar uma tabela
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {user} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )''')

    conn.commit()

async def add_item(user, item: dict): # Função que vai adicionar um item na tabela
    cursor.execute(f'''
    INSERT INTO {user} (name, price)
    VALUES (?, ?)
    ''', (item['name'][0], item['price'][0]))

    conn.commit()



