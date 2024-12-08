from playwright.async_api import async_playwright

import asyncio

async def verify_commerce(link): # Função que vai verificar qual é o e-commerce
    # Abre o playwright
    async with async_playwright() as p: 
        browser = await p.chromium.launch(headless=True)  # Abre uma pagina no chromium
        page = await browser.new_page()  

        await page.goto(link) 

        title = await page.title()

        await browser.close()

        if "Frete grátis" in title:
            return "MercadoLivre"

        if "Samsung Brasil" in title:
            return "Samsung"

        if "Amazon" in title:
            return "Amazon"

        if "AliExpress" in title:
            return "AliExpress"

        return title

async def data_get(link):
    commerce = await verify_commerce(link)

    if commerce == "MercadoLivre":
        return await is_mercadolivre(link)

    if commerce == "Samsung":
        return await is_samsung(link)

    if commerce == "Amazon":
        return await is_amazon(link)

    if commerce == "AliExpress":
        return await is_aliexpress(link)

    
async def is_mercadolivre(link):
    async with async_playwright() as p: 
        browser = await p.chromium.launch(headless=True)  # Abre uma pagina no chromium
        page = await browser.new_page()  

        await page.goto(link) 

        await page.locator('//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/h1').text_content()
        await page.locator('//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[2]').text_content()

        name_quotes: list = await page.locator('//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/h1').text_content()
        price_quotes: list = await page.locator('//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[2]').text_content()

        await browser.close()



    return {
        "name" : [name_quotes],
        "price" : [price_quotes]
    }

async def is_samsung(link):
    async with async_playwright() as p: 
        browser = await p.chromium.launch(headless=True)  # Abre uma pagina no chromium
        page = await browser.new_page()  

        await page.goto(link) 

        await page.wait_for_selector(".samsungmaster-global-pdp-shop-4-x-productName")
        await page.wait_for_selector(".samsungmaster-global-pdp-shop-4-x-sellingPrice")

        name_quotes: list = await page.query_selector_all(".samsungmaster-global-pdp-shop-4-x-productName")
        price_quotes: list = await page.query_selector_all(".samsungmaster-global-pdp-shop-4-x-sellingPrice")

        name: list = await asyncio.gather(*(quote.inner_text() for quote in name_quotes)) # Espera a coleta do nome do produto
        prices: list = await asyncio.gather(*(quote.inner_text() for quote in price_quotes)) # Espera a coleta do preço do produto

        await browser.close()

    return {
        "name" : name,
        "price" : [price[3:] for price in prices]
    }

async def is_amazon(link):
    async with async_playwright() as p: 
        browser = await p.chromium.launch(headless=True)  # Abre uma pagina no chromium
        page = await browser.new_page()  

        await page.goto(link) 

        await page.wait_for_selector("#productTitle")
        await page.wait_for_selector(".a-price-whole")

        name_quotes: list = await page.query_selector_all("#productTitle")
        price_quotes: list = await page.query_selector_all(".a-price-whole")

        name: list = await asyncio.gather(*(quote.inner_text() for quote in name_quotes)) # Espera a coleta do nome do produto
        prices: list = await asyncio.gather(*(quote.inner_text() for quote in price_quotes)) # Espera a coleta do preço do produto

        await browser.close()


    price = []
    for _ in prices[0]:
        if not _ in "1234567890.":
            break
        else:
            price.append(_)

    return {
        "name" : name,
        "price" : ["".join(price)]
    }

async def is_aliexpress(link):
    async with async_playwright() as p: 
        browser = await p.chromium.launch(headless=True)  # Abre uma pagina no chromium
        page = await browser.new_page()  

        await page.goto(link) 

        await page.locator('//*[@id="root"]/div/div[1]/div/div[1]/div[1]/div[2]/div[5]/h1').text_content()
        await page.locator('//*[@id="root"]/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/span').text_content()

        name_quotes: list = await page.locator('//*[@id="root"]/div/div[1]/div/div[1]/div[1]/div[2]/div[5]/h1').text_content()
        price_quotes: list = await page.locator('//*[@id="root"]/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/span').text_content()

        await browser.close()

    return {
        "name" : [name_quotes],
        "price" : [price_quotes]
    }


asyncio.run(is_mercadolivre("https://www.mercadolivre.com.br/motorola-edge-40-neo-5g-dual-sim-256-gb-black-beauty-8-gb-ram/p/MLB27865282#polycard_client=recommendations_home_navigation-trend-recommendations&reco_backend=machinalis-homes-univb&wid=MLB3516676249&reco_client=home_navigation-trend-recommendations&reco_item_pos=5&reco_backend_type=function&reco_id=13320e28-8143-4e7e-a80c-710be0c27d82&sid=recos&c_id=/home/navigation-trend-recommendations/element&c_uid=1eeade9d-dea7-46e7-95ab-7793a033be9e"))