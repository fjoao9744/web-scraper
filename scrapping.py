''' Importações '''
from playwright.async_api import async_playwright
import asyncio

''' Coleta de dados '''
async def data_get(link: str) -> dict: # Função que vai pegar o nome e os preços do produto
    try:
        # Abre o playwright
        async with async_playwright() as p:
            # Abre uma pagina do chromium para coletar os dados
            browser: object = await p.chromium.launch(headless=True)
            page: object = await browser.new_page()

            # Acessa a pagina
            await page.goto(link)

            # Espera os itens da pagina carregar
            await page.wait_for_selector(".samsungmaster-global-pdp-shop-4-x-productName")
            await page.wait_for_selector(".samsungmaster-global-pdp-shop-4-x-sellingPrice")

            # Coleta todas os itens
            name_quotes: list = await page.query_selector_all(".samsungmaster-global-pdp-shop-4-x-productName")
            price_quotes: list = await page.query_selector_all(".samsungmaster-global-pdp-shop-4-x-sellingPrice")

            name: list = await asyncio.gather(*(quote.inner_text() for quote in name_quotes)) # Espera a coleta o nome do produto
            prices: list = await asyncio.gather(*(quote.inner_text() for quote in price_quotes)) # Espera a coleta o preço do produto

            # Fecha a pagina
            await browser.close()

        return {
            "name" : name,
            "price" : [price[3:] for price in prices]
        }
        
    except:
        return "Não foi possivel coletar os dados"

