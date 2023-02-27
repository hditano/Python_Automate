import json
import requests

def My_API():

    r = requests.get('https://dummyjson.com/products')
    r.status_code

    load = json.loads(r.text)

    for item in load["products"]:
        print(f'Item: {item["title"]} | Price: ${item["price"]}')

My_API()
