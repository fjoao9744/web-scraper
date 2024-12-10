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
        price REAL NOT NULL,
        scrap TEXT NOT NULL
    )''')

    conn.commit()

async def add_item(user, item: dict, flag): # Função que vai adicionar um item na tabela
    cursor.execute(f'''
    INSERT INTO {user} (name, price, scrap)
    VALUES (?, ?, ?)
    ''', (item['name'][0], item['price'][0], flag))

    conn.commit()

async def last_item(user):
    cursor.execute(f'''
    SELECT name, price FROM {user}
        ORDER BY id DESC
        LIMIT 1
    ''')

    last_product = cursor.fetchone()

    return last_product

