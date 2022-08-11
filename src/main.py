import requests
import logging
from bs4 import BeautifulSoup

request = requests.get('https://e24.no/bors/aksjer/delayed?sort=displayName&size=1000')

if request.status_code==200:
    soup = BeautifulSoup(request.content, 'html.parser')
    print(soup.prettify())
else:
    print('ERROR: Responscode from e24 is not equal to 200.')
