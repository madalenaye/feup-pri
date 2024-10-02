from bs4 import BeautifulSoup
import urllib.request
import json 
from utils import fetchText, api_url




# Gets the character text from the html for a character
# Arg api_url: string url
# Arg name: string name of the character
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


print(get_character_character(api_url,"Ash_Ketchum"))