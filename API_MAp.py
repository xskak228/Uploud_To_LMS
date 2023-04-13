import json
import requests
from io import BytesIO
from PIL import Image

city = "MineralnieVody"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": city,
    "format": "json"}
response = requests.get("http://geocode-maps.yandex.ru/1.x/", params=geocoder_params)
json_response = response.json()

pos = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['Point']['pos']

lon, lat = pos.split(" ")
delta = "0.03"
params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
    "l": "map"
}
response = requests.get("http://static-maps.yandex.ru/1.x/", params=params)

with open("test.jpg", 'wb') as file:
    file.write(response.content)