import geocoder
import sys
from io import BytesIO
import requests
from PIL import Image

toponym_to_find = " ".join(sys.argv[1:])

ll, spn = geocoder.get_ll_span(toponym_to_find)

long, latti = geocoder.get_coordinates(toponym_to_find)

map_params = {
    "ll": ll,
    "spn": spn,
    "l": "map",
    'pt': f'{long},{latti},org'
}

map_api_server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
