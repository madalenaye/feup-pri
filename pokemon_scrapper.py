from bs4 import BeautifulSoup
from utils import fetchText, api_url


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
        list_of_pokemon.append((pokedex_entry, pokemon, pokemon_page))
    return list_of_pokemon

def get_pokemon_blurb(html, name):
    text = ""
    soup = BeautifulSoup(html, "html.parser")
    beforeBlurb = soup.select('div.mw-parser-output > table')[1]
    sibling = beforeBlurb.find_next_sibling()
    while sibling.name != "div":
        if sibling.name == "p":
            text += sibling.text.strip() + " "
        phrases = sibling.find_all("p")
        for p in phrases:
            plot += str(p.text.strip())
        sibling = sibling.find_next_sibling()
    return text

#print(get_list_pokemon(api_url, 'List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'))

def main():
    #print(get_list_pokemon(api_url, 'List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'))
    all = get_list_pokemon(api_url, 'List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number')
    test = all[43][2]
    url = fetchText(api_url+test)
    test1 = get_pokemon_blurb(url, 'a')
    print(test1)

main()