from bs4 import BeautifulSoup
from utils import fetchText, api_url, remove_references


def get_list_pokemon(api_url, page):
    html = fetchText(api_url+page)
    soup = BeautifulSoup(html, "html.parser")
    fetch = soup.find_all('tr', style='background:#FFF')
    list_of_pokemon = []
    for i in fetch:
        if i.contents[1].text.strip() == '':
            continue
        pokedex_entry = i.contents[1].text.strip()
        pokemon = i.contents[5].find('a').text.strip()
        pokemon_page = i.contents[3].find('a').get('href').split('/')[-1]
        pokemon_types = [i.contents[7].find('a').text.strip(), i.contents[9].find('a').text.strip() if len(i.contents) > 9 else None]
        list_of_pokemon.append((pokedex_entry, pokemon, pokemon_page, pokemon_types))
    return list_of_pokemon

def get_pokemon_blurb(html, name):
    text = ""
    soup = BeautifulSoup(html, "html.parser")
    before_blurb = soup.select('div.mw-parser-output > table')[1]
    sibling = before_blurb.find_next_sibling()
    if sibling.name == "p":
        while sibling.name != "div":
            if sibling.name == "p":
                text += remove_references(sibling.text.strip()) + " "
            phrases = sibling.find_all("p")
            for p in phrases:
                plot += remove_references(str(p.text.strip()))
            sibling = sibling.find_next_sibling()
    else:
        raise Exception("Blurb section not found for given pokemon: " + name)
    return text

def get_pokemon_biology(html, name):
    text = ""
    soup = BeautifulSoup(html, "html.parser")
    before_biology = soup.find("div", class_='thumb tleft')
    biology = before_biology.find_next_sibling()
    if biology.name == "p":
        while biology.name != "h3":
            if biology.name == "p":
                text += remove_references(biology.text.strip()) + " "
                phrases = biology.find_all("p")
                for p in phrases:
                    text += remove_references(str(p.text.strip()))
            biology = biology.find_next_sibling()
    else:
        raise Exception("Biology section not found for given pokemon: " + name)
    return text

def get_pokemon_stats(html, name):
    soup = BeautifulSoup(html, "html.parser")
    pokemon_stats = []
    pokemon_abilities = []
    table = soup.select('div.mw-parser-output > table')[1]
    table_body = table.find('tbody')
    ability_row = table_body.contents[4].find_all('td')
    for i in ability_row:
        if i.find('a') is not None and "style" not in i.attrs:
            pokemon_abilities.append(i.find('a').text.strip())
    image_row = table_body.contents[0].find_all('td')
    for i in image_row:
        a = i.find('a', class_="image")
        if a and ("style" not in i.attrs):
            img = a.find('img').get('src')
            pokemon_stats.append(img)
            break
    pokemon_stats.append(pokemon_abilities)
    return pokemon_stats

