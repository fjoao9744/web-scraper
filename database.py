from peewee import *

# Conectar ao banco de dados SQLite
db = SqliteDatabase('database.db')

class Product(Model):
    user = CharField(unique=True) # Usuario que vai requerir o produto
    name = CharField() # Nome do produto
    price = BooleanField() # Preço do produto

    class Meta:
        database = db # Define que essa tabela está no banco 'db'

        # Conecta ao banco de dados
db.connect()

# Cria as tabelas no banco de dados
db.create_tables([Product])

# Fecha a conexão com o banco de dados
db.close()