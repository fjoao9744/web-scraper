''' Importações '''
from playwright.sync_api import sync_playwright
import asyncio

''' Coleta de dados '''
def data_get(link: str) -> dict: # Função que vai pegar o nome e os preços do produto
    # Abre o playwright
    with sync_playwright() as p:
        # Abre uma pagina do chromium para coletar os dados
        browser: object = p.chromium.launch(headless=True)
        page: object = browser.new_page()

        # Acessa a pagina
        page.goto(link)

        # Espera os itens da pagina carregar
        page.wait_for_selector(".samsungmaster-global-pdp-shop-4-x-productName")
        page.wait_for_selector(".samsungmaster-global-pdp-shop-4-x-sellingPrice")

        # Coleta todas os itens
        name_quotes: list = page.query_selector_all(".samsungmaster-global-pdp-shop-4-x-productName")
        price_quotes: list = page.query_selector_all(".samsungmaster-global-pdp-shop-4-x-sellingPrice")

        name: list = [quote.inner_text() for quote in name_quotes] # Coleta o nome do produto
        price: list = [quote.inner_text()[3:] for quote in price_quotes] # Coleta o preço do produto

        # Fecha a pagina
        browser.close()


    return {
        "name" : name,
        "price" : price
    }

print(data_get("https://shop.samsung.com/br/monitor-curvo-full-hd-samsung-led-27/p"))