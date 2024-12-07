''' Importações '''
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import asyncio

''' Verificação de e-commerce '''
async def verify_commerce(link: str): # Função que vai verificar qual é o e-commerce do link
    async with async_playwright() as p:
        browser: object = await p.chromium.launch(headless=True)
        page: object =  await browser.new_page()

        # Acessa a pagina
        await page.goto(link)

        title = await page.title()
        
        if title[-14:] in "Samsung Brasil":
            return {
                "name": ".samsungmaster-global-pdp-shop-4-x-productName",
                "price": ".samsungmaster-global-pdp-shop-4-x-sellingPrice"
                }
        
        await browser.close()

''' Coleta de dados '''
async def data_get(link: str) -> dict: # Função que vai pegar o nome e os preços do produto
    selectors: dict = await verify_commerce(link)
    try:
        # Abre o playwright
        async with async_playwright() as p:
            # Abre uma pagina do chromium para coletar os dados
            browser: object = await p.chromium.launch(headless=True)
            page: object = await browser.new_page()

            # Acessa a pagina
            await page.goto(link)

            # Espera os itens da pagina carregar
            await page.wait_for_selector(selectors['name'])
            await page.wait_for_selector(selectors['price'])

            # Coleta todas os itens
            name_quotes: list = await page.query_selector_all(selectors['name'])
            price_quotes: list = await page.query_selector_all(selectors['price'])

            name: list = await asyncio.gather(*(quote.inner_text() for quote in name_quotes)) # Espera a coleta do nome do produto
            prices: list = await asyncio.gather(*(quote.inner_text() for quote in price_quotes)) # Espera a coleta do preço do produto

            # Fecha a pagina
            await browser.close()
        
        return {
            "name" : name,
            "price" : [price[3:] for price in prices]
        }
        
    except:
        return "Não foi possivel coletar os dados"
