''' Importações '''
from bs4 import BeautifulSoup
import requests
import asyncio

''' Coleta e filtragem de html '''
def get_html(url: str) -> str: # Função que recebe um link e retorna o html daquele link
    html = requests.get(url) # Faz uma requisição no link passado como argumento

    return html.text # Retorna um texto com todo o html da pagina

def request_api(api_url: str) -> str:

    response = requests.get(api_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
    data = response.json()
    prices = []
    for _ in data:
        print(_)
    

def get_html_tag(link: str) -> dict: # Função que vai pegar os dados das tags
    page = get_html(link)

    soup = BeautifulSoup(page, "html.parser")
    name = soup.find("h2", class_="samsungmaster-global-pdp-shop-4-x-productName").get_text()
    price = request_api("https://shop.samsung.com/br/api/catalog_system/pub/products/search/?fq=productId:2322")

    return {
        "name" : name,
        "price" : price
    }

print(get_html_tag("https://shop.samsung.com/br/monitor-curvo-full-hd-samsung-led-27/p?idsku=525&utm_source=google&utm_medium=ppc&utm_campaign=br_pd_ppc_prfmx_mon-multi_ecommerce_cad19-a5002-vd-opn_pla_none_paid-cdm-pfm-IDnone-{product-id}&utm_content=pla-prfmx&utm_term=na&cid=br_pd_ppc_prfmx_mon-multi_ecommerce_cad19-a5002-vd-opn_pla_none_paid-cdm-pfm-IDnone-{product-id}&keeplink=true&gad_source=1"))