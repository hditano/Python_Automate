import requests
import re
from bs4 import BeautifulSoup

def My_Test():

    pattern = 'mt'

    my_search = re.compile(pattern)

    URL = "https://www.ole.com.ar/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("div", {"class":my_search})

    for items in results:
        if re.search(r'essi\b', items.text):
            print(items.text)


def Google_Search():

    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win65; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    
    URL = 'https://google.com/search?q='

    UserInput = 'Argentina'

    page = requests.get(URL + UserInput, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    for item in soup.find_all("div", {"class": "yuRUbf"}):
        egida = item.find_next("h3").get_text()
        print(egida)
    
Google_Search()
