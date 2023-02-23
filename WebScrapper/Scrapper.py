import requests
from bs4 import BeautifulSoup

def My_Test():
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.findAll(class_="title is-5")

    for item in results:
        print(item.text)
My_Test()
