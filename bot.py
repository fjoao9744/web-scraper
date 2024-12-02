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

''' Função executada quando o bot ligar '''
@bot.event
async def on_ready() -> None:
    print(f"Bot {bot.user} está online!")

''' Função executada quando o bot entra em um servidor '''
@bot.event
async def on_guild_join(guild) -> None:
    # Encontra um canal de texto específico para enviar a mensagem
    for _ in guild.text_channels:
        if _.permissions_for(guild.me).send_messages:  # Verifica se o bot tem permissão para enviar mensagens
            channel: object = _
            break # Acha o primeiro canal disponível

    if channel: # Se achar um canal disponivel envia a mensagem
        await channel.send(f"Olá! Eu sou o Web Scraper e fui desenvolvido para realizar a tarefa de web scraping, para começar basta apenas digitar `!play` para receber mais informações no privado.")
    
''' Comando scraping '''
@bot.command()
async def scraping(ctx, *, message: str) -> None:
    if ctx.guild == None:
        loading: str = await ctx.send("Coletando dados do produto... aguarde...")

        try:
            product: dict = await data_get(message)
            await ctx.send(f"**Produto:** {product['name'][0]}\n**Preço:** {product['price'][0]}" if len(product['name']) == 1 and len(product['price']) == 1 else f"**Produto:** {product['name']} \n**Preço:** {product['price']}") # Se tiver mais de um nome ou preço ele vai mostrar uma lista com os itens
            
        except:
            await ctx.send("O link do produto é invalido.")

''' Comando play '''
@bot.command()
async def play(ctx) -> None:
    if not ctx.guild == None: # Se não for enviado no privado ele vai mostrar a mensagem
        await ctx.author.send("Ola! esta pronto para monitorar o preço de qualquer produto? é só digitar o comando '!scraping' e colocar a URL do produto que deseja verificar e pronto! o preço do produto sera enviado para você de 5 em 5 horas ")

''' Carregamento do token '''
load_dotenv() # Carrega as variaveis de ambiente

token: str = os.getenv("BOT_TOKEN") # Token

''' Roda o bot com o token'''
def bot_run() -> None:
    bot.run(token) # Liga o bot

bot_run()