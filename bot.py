''' Importações '''
import discord
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv
from scrapping import data_get

''' Configurações padrão do bot '''
intents: object = discord.Intents.default() 
intents.message_content = True  # Permite que o bot leia mensagens
intents.members = True  # Permite que o bot acesse eventos relacionados a membros

''' Variavel para gerenciar os comandos do bot '''
bot: object = commands.Bot(command_prefix="!", intents=intents)

''' Função executada quando o bot ligar'''
@bot.event
async def on_guild_join(guild: object) -> str:
    print(f'Bot {bot.user} está online!')
    user: object = guild.owner

    if user:
        await user.send("Ola! esta pronto para monitorar o preço de qualquer produto? é só digitar o comando '!scraping' e colocar a URL do produto que deseja verificar e pronto! o preço do produto sera enviado para você de 5 em 5 horas ")

''' Comando scrap '''
@bot.command()
async def scraping(ctx, *, message: str) -> str:
    product = await data_get(message)
    await ctx.send(product)

''' Carregamento do token '''
load_dotenv() # Carrega as variaveis de ambiente

token: str = os.getenv("BOT_TOKEN") # Token

''' Roda o bot com o token'''
def bot_run():
    bot.run(token) # Liga o bot

bot_run()