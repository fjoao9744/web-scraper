from scrapping import data_get
import asyncio

async def main():
    product = await data_get("https://shop.samsung.com/br/monitor-curvo-full-hd-samsung-led-27/p")

    print(product)

asyncio.run(main())