import requests
from bs4 import BeautifulSoup

class Scraper:
    url = 'https://e24.no/bors/aksjer/delayed?sort=displayName&size=1000'

    def __init__(self):
        pass
 
    def scrape(self):
        request = requests.get(self.url)
        if request.status_code==200:
            soup = BeautifulSoup(request.content, 'html.parser')
            print(soup.prettify())
        else:
            print('ERROR: Responscode from e24 is not equal to 200. Current responscode: ' + request.status_code)