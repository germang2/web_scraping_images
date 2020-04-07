import requests
import json

url = "https://dog.ceo/api/breeds/image/random"


r = requests.get(url)

if r.status_code == 200:
    data = json.loads(r.text)
    url_image = data['message']
    req_image = requests.get(url_image)
    if req_image.status_code == 200:
        with open('images/dog_image.jpg', 'wb') as image:
            image.write(req_image.content)