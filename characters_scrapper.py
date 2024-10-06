from bs4 import BeautifulSoup
import urllib.request
import json 
from utils import fetchText, api_url

# Gets the list of characters from the list page
# Arg api_url: string url
# Arg page: string page name
# Return: list of tuples (character,character_page,ep,role)
def get_list_characters(api_url,page):
    list_of_characters=[]
    html = fetchText(api_url+page)
    soup = BeautifulSoup(html,"html.parser")
    section = soup.find(id="Original_series")
    tables = section.find_all_next("table")
    for table in tables:
        if table.find_previous("h2").find("a").text.strip() == "Movies":
            break
        
        rows = table.find_all("tr")
        for row in rows[1:]:
            cells = row.find_all_next("td")
            character = cells[0].find("a").text.strip()
            print(character)
            character_page = cells[0].find("a").get("href").split("/")[-1]
            ep = cells[1].find("a").get("href").split("/")[-1]
            role = cells[2].text.strip()
            list_of_characters.append((character,character_page,ep,role))
    return list_of_characters
        
# Gets the character text from the html for a character
# Arg api_url: string url
# Arg name: string name of the character
# Return: string text of the character
def get_character_character(api_url,name):
    text=""
    html = fetchText(api_url+name)
    soup = BeautifulSoup(html,"html.parser")
    character_section = soup.find(id="Character")
    if character_section:
        sibling=character_section.find_next("p")
        while sibling.name != "h3":
            if(sibling.name == "p"):
                text += sibling.text.strip() 
            sibling = sibling.find_next_sibling()
    else:
        raise Exception("Character section not found for given character: "+name)
    return text

def get_character_history(api_url,name):
    text=""
    html = fetchText(api_url+name)
    soup = BeautifulSoup(html,"html.parser")
    history_section = soup.find(id="History")
    if history_section:
        sibling=history_section.find_next("p")
        while sibling.name != "h3":
            if(sibling.name == "p"):
                text += sibling.text.strip() 
            sibling = sibling.find_next_sibling()
    
    else:
        raise Exception("History section not found for given character: "+name)
    
    return text
# Gets the table info from the html for a character
# Arg api_url: string url
# Arg name: string name of the character
def get_character_table_info(api_url,name):
    table = {}
    html = fetchText(api_url+name)
    soup = BeautifulSoup(html,"html.parser")
    character_table_section = soup.find("big")
    if character_table_section:
        character_table = character_table_section.find_parent("table")
        if character_table:
            rows = character_table.find_all("tr")
            name = rows[0].find("big")
            table["Name"]=name.text.strip()
            japanese_name_translation = name.find_next("i")
            japanese_name = japanese_name_translation.find_previous_sibling()

            if japanese_name:
                table["Japanese Name"]=japanese_name.text.strip() + " " +"("+japanese_name_translation.text.strip()+")"
            for row in rows[1:]:
                key = row.find("th")
                value = row.find("td")
                if(key and value):
                    table[key.text.strip()] = value.text.strip()
        else:
            raise Exception("Table not found for given character: "+name)
    else:
        raise Exception("Table section not found for given character: "+name)
    return table


