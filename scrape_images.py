import requests
import json

url = "https://dog.ceo/api/breeds/image/random"

r = requests.get(url)

if r.status_code == 200:
    data = json.loads(r.text)
    print(data)