from scrapping import data_get
import asyncio

async def main():
    product = await data_get("https://www.amazon.com.br/Creme-Hidratante-453-G-Cetaphil/dp/B079VXJK79/ref=cm_gf_aabk_iaad_d_p0_e0_qd0_MYV46bXKoFvyyrTWJRX4?sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D")

    print(product)
    product = await data_get("https://pt.aliexpress.com/item/1005007918633378.html?spm=a2g0o.tm1000009216.d5.1.2d016f3dRFGcEQ&sourceType=561&pvid=3448bf6d-c57c-4b16-9518-f83fc7c47d2c&pdp_ext_f=%7B%22ship_from%22:%22CN%22,%22sku_id%22:%2212000042844136157%22%7D&scm=1007.28480.379202.0&scm-url=1007.28480.379202.0&scm_id=1007.28480.379202.0&pdp_npi=4%40dis%21BRL%21R%24%20181%2C23%21R%24%2051%2C62%21%21%21209.47%2159.66%21%402103241117336621183758497e6c07%2112000042844136157%21gsd%21BR%21%21X&channel=sd&aecmd=true&_gl=1*8daruu*_gcl_au*MTQyNTYyODIzNC4xNzMzNjE4Nzgy*_ga*MTI4NDM0OTE4OS4xNzMzNjE4Nzgy*_ga_VED1YSGNC7*MTczMzY2MjA0MC4yLjEuMTczMzY2MjU4NS41Mi4wLjA.")

    print(product)
    product = await data_get("https://shop.samsung.com/br/galaxy-z-fold6/p")

    print(product)

asyncio.run(main())