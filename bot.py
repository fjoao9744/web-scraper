''' Importações '''
import discord
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv

''' Configurações padrão do bot '''
intents: object = discord.Intents.default() 
intents.message_content = True  # Permite que o bot leia mensagens
intents.members = True  # Permite que o bot acesse eventos relacionados a membros

''' Variavel para gerenciar os comandos do bot '''
bot: object = commands.Bot(command_prefix="! ", intents=intents)

''' Função executada quando o bot ligar'''
async def bot_on() -> None:
    print(f'Bot {client.user} está online!')

''' Carregamento do token '''
load_dotenv() # Carrega as variaveis de ambiente

token = os.getenv("BOT_TOKEN") # Token

''' Roda o bot com o token'''
if __name__ == "__main__":
    bot.run(token) # Liga o bot