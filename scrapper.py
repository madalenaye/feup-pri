from bs4 import BeautifulSoup
import urllib.request
import json 
episodes_url ='https://bulbapedia.bulbagarden.net/wiki/List_of_animated_series_episodes'
def get_list_episodes(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        soup = BeautifulSoup(url, 'html.parser')
        fetch = soup.find_all('tr',style="text-align:center; background:#FFFFFF")
        return [i.contents[1].text.strip() for i in fetch]

def fetchText(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        return json.load(url)["parse"]["text"]["*"]

def getPlot(soup):
    plot = ""
    plotHeader = soup.find(id="Plot").parent
    sibling = plotHeader.find_next_sibling()
    while sibling.name == "p":
        plot += str(sibling).strip()
        sibling = sibling.find_next_sibling()

    return plot

print(getPlot(BeautifulSoup(fetchText('https://bulbapedia.bulbagarden.net/w/api.php?action=parse&format=json&page=EP041'), "html.parser")))
