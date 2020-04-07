import requests
import json

url = "https://dog.ceo/api/breeds/image/random"


for i in range(1, 6):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = json.loads(r.text)
            url_image = data['message']
            req_image = requests.get(url_image)
            if req_image.status_code == 200:
                with open(f'images/dog_image{i}.jpg', 'wb') as image:
                    image.write(req_image.content)
                    print(f'image number {i} written successfully')
    except Exception as exp:
        print(f'Fail getting image number {i}')
        print(exp)
