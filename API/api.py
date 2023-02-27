import json
import requests
import sys

def My_API():

    r = requests.get('https://dummyjson.com/products')
    r.status_code

    status = sys.argv[1:]

    load = json.loads(r.text)

    print(status)

    for item in load["products"]:
        print(f'Item: {item["title"]} | Price: ${item["price"]}')

My_API()
