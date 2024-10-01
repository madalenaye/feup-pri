from bs4 import BeautifulSoup
import urllib.request
import json 

req =urllib.request.Request('https://bulbapedia.bulbagarden.net/w/api.php?action=parse&format=json&page=EP041', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as url:
    data = json.load(url)
    
    print(data["parse"]["text"]["*"])
