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
        for row in rows:
            cells = row.find_all_next("td")
            character = cells[0].find("a").text.strip()
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
            
    return text


#print(get_character_character(api_url,"Ash_Ketchum"))
print(get_list_characters(api_url,"List_of_animated_series_characters#Original_series"))