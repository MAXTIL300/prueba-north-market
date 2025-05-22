import requests
from bs4 import BeautifulSoup


def buscar_mercado_libre(palabra):
    url = f'https://listado.mercadolibre.com.co/{palabra}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error al obtener la página")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    productos = soup.select('div.ui-search-result__wrapper')[:5]

    for i, producto in enumerate(productos, 1):
        titulo = producto.select_one('h2.ui-search-item__title')
        precio = producto.select_one('span.price-tag-fraction')

        titulo_text = titulo.text.strip() if titulo else "Sin título"
        precio_text = precio.text.strip() if precio else "Sin precio"

        print(f"{i}. {titulo_text} - Precio: ${precio_text}")


if __name__ == "__main__":
    # Cambiar solicitud de búsqueda aquí
    palabra = "iphone 13"
    buscar_mercado_libre(palabra)
