''' Importações '''
import sqlite3
import asyncio

''' Conecção e cursor com o DB '''
conn = sqlite3.connect('database.db') # Estabelece conecção com o banco de dados
cursor = conn.cursor() # Cria um cursor para interagir com a tabela

''' Funções para interação com o DB '''
async def create_table(user: str): # Função que vai criar uma tabela
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



