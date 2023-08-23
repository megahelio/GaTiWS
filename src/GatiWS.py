import requests
from html import unescape
from lxml import html
import sys
from datetime import datetime 
if __name__ == "__main__":
    if "-date" in sys.argv:
        date = sys.argv[sys.argv.index("-date") + 1]
    else:
        # Obtener la fecha actual
        today = datetime.now().strftime('%d/%m/%Y')
        date = input(f"Date To Search [{today}]:") or today

    # URL de la petición
    url = "https://www.meteogalicia.gal/web/predicion/maritima/listMaritimaTaboa.action"
    # Datos del cuerpo de la petición
    payload = {
        "data": date
    }
    # Realizar la petición POST
    response = requests.post(url, data=payload)
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener el contenido HTML
        html_content = unescape(response.content.decode('utf-8'))
        ruta=""
        with open(ruta, "w",  encoding="utf-8") as f:
            f.write(html_content)
        print(html_content)
    else:
        print("Error al realizar la solicitud HTTP.")


