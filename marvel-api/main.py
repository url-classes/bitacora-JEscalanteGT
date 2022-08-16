import hashlib
import requests
import time

endpoint = 'https://gateway.marvel.com/v1/public/'
resource = 'characters'
timestamp = time.time()
public_key = '1aa848defd6e3980f0a4ddd5c01af610'
secret_key = 'd119b3af5741101a8ce81a010be86cb7ca6e2ca8'

access = f"{timestamp}{secret_key}{public_key}"
ultra_secret = hashlib.md5(access.encode())

authentication = {
    "apikey": public_key,
    "ts": timestamp,
    "hash": ultra_secret.hexdigest()
}

response = requests.get(f"{endpoint}{resource}", params=authentication)

r = response.json()
results = r["data"]["results"]
total = r["data"]["count"]
for character in results:
    print(character["name"])
