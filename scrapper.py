from bs4 import BeautifulSoup
import urllib.request
import json 

episodes_url = 'https://bulbapedia.bulbagarden.net/w/api.php?action=parse&format=json&page=List_of_animated_series_episodes'
api_url= 'https://bulbapedia.bulbagarden.net/w/api.php?action=parse&format=json&page='

def get_list_episodes(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        html = json.load(url)["parse"]["text"]["*"]
        soup = BeautifulSoup(html, 'html.parser')
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
    while sibling.name != "h2":
        if(sibling.name == "p"):
            plot += sibling.text.strip()
        phrases = sibling.find_all("p")
        for p in phrases:
            plot += str(p.text.strip())
        sibling = sibling.find_next_sibling()
    return plot

def get_plot_from_episode(episode):
    html = fetchText(api_url+episode)
    soup = BeautifulSoup(fetchText(api_url+episode),"html.parser")

    return getPlot(soup)

print(get_plot_from_episode("EP041"))
