import requests
import asyncio

async def get_html(link) -> str: # Função que recebe um link e retorna o html daquele link
    html = requests.get(link)

    
