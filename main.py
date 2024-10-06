from characters_scrapper import *
from series_scrapper import * 
from utils import *
import pandas as pd 
import json

# Writes to a document unprocessed data

def scrape_episodes(num):
    with open("documents/episodes.json","w") as json_file:
        final_document={}
        for episode in get_list_episodes(api_url,'List_of_animated_series_episodes'):
            print(episode)
            try:
                episode_info = get_table(BeautifulSoup(fetchText(api_url+episode),"html.parser"))
                episode_info["Characters"] = get_characters(api_url,episode)
                episode_info["Plot"] = get_plot_from_episode(api_url,episode)

                final_document[episode]=episode_info
            except Exception as error:
                print("Error in episode: "+episode)
                print(error)
                print("-------")
                continue
            finally:
                num -= 1
                if num <= 0:
                    break
        json.dump(final_document,json_file)

def scrape_characters(num):
    with open("documents/characters.json","w") as json_file:
        final_document={}
        for character,character_code,first_appearance,role in get_list_characters(api_url,"List_of_animated_series_characters#Original_series"):
            print(character,character_code,first_appearance,role)
            try:
                character_info = get_character_table_info(api_url,character_code)
                character_info["Character Code"] = character_code
                character_info["Role"] = role
                character_info["First Appearance"]=first_appearance
                character_info["Character"]=get_character_character(api_url,character_code)
                character_info["History"]=get_character_history(api_url,character_code)
                final_document[character]=character_info
            except Exception as error:
                print("Error in character: "+character)
                print(error)
                print("-------")
                continue
            finally:
                num -= 1
                if num <= 0:
                    break
        json.dump(final_document,json_file)

scrape_characters(5)