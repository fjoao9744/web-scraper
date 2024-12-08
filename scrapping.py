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
        print(title)

        if "MercadoLivre" in title:
            return "MercadoLivre"

        if "Samsung Brasil" in title:
            return "Samsung"

        if "Amazon" in title:
            return "Amazon"

        if "SHEIN" in title or "shein" in title or "Shein" in title:
            return "Shein"

        if "Attention Required!" in title:
            return "OLX"
        
        if "AliExpress" in title:
            return "AliExpress"

        return title


