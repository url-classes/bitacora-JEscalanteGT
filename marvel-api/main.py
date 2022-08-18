import hashlib
import requests
import time
import math

# Autenticación para la API
endpoint = 'https://gateway.marvel.com/v1/public/'
resource = 'characters'
timestamp = time.time()
public_key = '1aa848defd6e3980f0a4ddd5c01af610'
secret_key = 'd119b3af5741101a8ce81a010be86cb7ca6e2ca8'
access = f"{timestamp}{secret_key}{public_key}"
ultra_secret = hashlib.md5(access.encode())

# Variables de control
total_pages = 0


def get_characters(page, limit):
    global total_pages

    params = {
        "apikey": public_key,
        "ts": timestamp,
        "hash": ultra_secret.hexdigest(),
        "limit": limit,
        "offset": page * limit
    }

    response = requests.get(f"{endpoint}{resource}", params=params)
    data = response.json()["data"]
    total = data["total"]
    total_pages = math.ceil(total / limit)
    characters = data["results"]

    return characters


def main():
    page = 0
    limit = 20
    characters = get_characters(page, limit)
    while True:
        print('Personajes:')
        for character in characters:
            print(character["name"])
        print(f"Página {page} de {total_pages}")
        print('1- Página siguiente')
        print('2- Página anterior')
        print('3- Página en específico')
        print('4- Salir')
        option = int(input('Ingrese una opción: '))

        if option == 1:
            page = page + 1
            characters = get_characters(page, limit)
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            break
        else:
            continue


main()
