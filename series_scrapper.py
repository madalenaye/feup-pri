from bs4 import BeautifulSoup

from utils import fetchText

# Gets the list of episodes from the API as ep codes (ex:EP001)
# Arg url: string url
# Arg page: string page name
# Return: list of episode codes
def get_list_episodes(api_url,page):
    soup = BeautifulSoup(fetchText(api_url+page), 'html.parser')
    fetch = soup.find_all('tr',style="text-align:center; background:#FFFFFF")
    return [i.contents[1].text.strip() for i in fetch]
    
# Gets the plot from the html
# Arg soup: BeautifulSoup object
# Return: string plot
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

# Gets the plot from the episode code
# Arg episode: string code of the episode
# Return: string plot
def get_plot_from_episode(html,episode):
    soup = BeautifulSoup(html,"html.parser")

    return getPlot(soup)

# Gets the table content from the episode page
# Arg soup: BeautifulSoup object
# Return: dict table of the episode info
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
      
# Gets the dict of characters and pokemons from the episode
# Arg api_url: string url
# Arg episode: string code of the episode
# Return: dict characters and pokemons
def get_characters(html,episode):
    characters={}
    soup = BeautifulSoup(html,"html.parser")
    characters_section = soup.find(id="Characters")

    humans = characters_section.find_next("h3")
    list_of_humans = humans.find_next("ul")
    humans_list = list_of_humans.find_all("li")
    characters["Humans"]= [i.text.strip() for i in humans_list]

    pokemons = humans.find_next("h3")
    list_of_pokemons = pokemons.find_next("ul")
    pokemons_list = list_of_pokemons.find_all("li")
    characters["Pokemons"]= [i.text.strip() for i in pokemons_list]
        
    return characters

def get_major_events(html, episode):
    major_events = []
    soup = BeautifulSoup(html, "html.parser")
    major_events = soup.find(id="Major_events")

    list_of_events = major_events.find_next("ul")
    major_events = [i.text.strip() for i in list_of_events if i.text.strip() != ""]

    return major_events
