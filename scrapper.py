from bs4 import BeautifulSoup
import urllib.request
import json 


def fetchText(url):
    req =urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        return json.load(url)["parse"]["text"]["*"]

print(fetchText('https://bulbapedia.bulbagarden.net/w/api.php?action=parse&format=json&page=EP041'))