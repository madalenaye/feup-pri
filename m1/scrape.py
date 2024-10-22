# Writes to a document unprocessed data of episodes
import json
import traceback
from bs4 import BeautifulSoup
from characters_scraper import get_character_character, get_character_history, get_character_table_info, get_list_characters
from pokemon_scraper import get_list_pokemon, get_pokemon_biology, get_pokemon_blurb, get_pokemon_stats
from series_scraper import get_characters, get_list_episodes, get_major_events, get_plot_from_episode, get_table
from utils import api_url, fetchText


def scrape_episodes(file):
    num = 276
    with open(file,"w") as json_file:
        final_document={}
        for episode in get_list_episodes(api_url,"List_of_animated_series_episodes"):
            print(episode)
            try:
                html = fetchText(api_url+episode)

                episode_info = get_table(BeautifulSoup(html,"html.parser"))
                episode_info["Characters"] = get_characters(html)
                episode_info["Plot"] = get_plot_from_episode(html)
                episode_info["Major events"] = get_major_events(html)

                final_document[episode]=episode_info
            except Exception as error:
                print("Error in episode: "+episode)
                print(error)
                print("-------")
                traceback.print_exc()
                continue
            finally:
                num -= 1
                if num <= 0:
                    break
        json.dump(final_document,json_file)
        return final_document

# Writes to a document unprocessed data of characters
def scrape_characters(file):
    with open(file,"w") as json_file:
        final_document={}
        for character,character_code,first_appearance,role in get_list_characters(api_url,"List_of_animated_series_characters#Original_series"):
            print(character,character_code,first_appearance,role)
            try:
                html = fetchText(api_url+character_code)

                character_info = get_character_table_info(html,character_code)
                #character_info["Character Code"] = character_code
                character_info["Name"] = character
                character_info["Role"] = role
                character_info["First Appearance"]=first_appearance
                character_info["Character"]=get_character_character(html,character_code)
                character_info["History"]=get_character_history(html,character_code)
                final_document[character_code]=character_info
                if character_code == "Captain_(EP274)":
                    break
            except Exception as error:
                print("Error in character: "+character)
                print(error)
                print("-------")
                continue
            #finally:
            #    num -= 1
            #    if num <= 0:
            #        break
        json.dump(final_document,json_file)
        return final_document
    
def scrape_pokemon(file):
    num = 251
    with open(file,"w") as json_file:
        final_document={}
        for pokedex_entry, pokemon, pokemon_page, pokemon_types in get_list_pokemon(api_url, 'List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'):
            try:
                html = fetchText(api_url+pokemon_page)
                pokemon_info = {}
                pokemon_info["Pokedex Entry"] = pokedex_entry
                pokemon_info["Pokemon Page"] = pokemon_page
                pokemon_info["Types"] = pokemon_types
                pokemon_info["Blurb"] = get_pokemon_blurb(html,pokemon)
                pokemon_info["Biology"] = get_pokemon_biology(html,pokemon)
                pokemon_info["Stats"] = get_pokemon_stats(html,pokemon)
                final_document[pokemon]=pokemon_info
                print(pokemon)
            except Exception as error:
                print("Error in pokemon: "+pokemon)
                print(error)
                print("-------")
                continue
            finally:
                num -= 1
                if num <= 0:
                    break
        json.dump(final_document,json_file)
        return final_document