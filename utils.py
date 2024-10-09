import urllib.request
import json 

api_url= 'https://bulbapedia.bulbagarden.net/w/api.php?action=parse&format=json&page='

# Gets html from the json provided by the url
# Arg url: string url
def fetchText(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        return json.load(url)["parse"]["text"]["*"]
def fetchField(url,field):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        return json.load(url)["parse"][field]
    
def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError