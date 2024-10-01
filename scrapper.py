from bs4 import BeautifulSoup
import urllib.request
import json 

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

def get_table(soup):
    table = {}
    tableHeader = soup.find("table", class_="roundy", style="float:right; display: table !important; background: #FFAAAA; width: 25%; margin-left: 5px; margin-bottom: 5px")
    
    ep_code = tableHeader.find("td", class_="roundy", width="25%",style="background: #AAFFAA;")
    table["Episode Code"]=ep_code.text.strip()

    title = tableHeader.find("big")
    table["Name"]=title.text.strip()

    subtitle = tableHeader.find("small")
    table["Subtitle"]=subtitle.text.strip()

    subtables = tableHeader.find_all("td", class_="roundy" ,style="background:#AAFFAA")
    for subtable in subtables:
        sub_header = subtable.find("b")
        if sub_header:
            table[sub_header.text.strip()]={}
            for th in subtable.find_all("th"):
                if th:
                    if(th.find_next_sibling()):
                        table[sub_header.text.strip()][th.text.strip()]= th.find_next_sibling().text.strip()
    ### I dont consider adicional credits, we need another approach otherwise
    return table          
            
        
i=0
#for episode in get_list_episodes(api_url+'List_of_animated_series_episodes'):
 #   if i==28:
  #      break
  #  print(get_plot_from_episode(episode))
  #  print("-----------------------------")
   # i-=1
for episode in get_list_episodes(api_url+'List_of_animated_series_episodes'):
    if i<=30:
        print(get_table(BeautifulSoup(fetchText(api_url+episode),"html.parser")))
        print("-----------------------------")
    else:
        break;
    i+=1