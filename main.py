from characters_scrapper import *
from series_scrapper import * 
from utils import *
import pandas as pd 
import json
import re
# Writes to a document unprocessed data of episodes
def scrape_episodes(num):
    with open("documents/episodes.json","w") as json_file:
        final_document={}
        for episode in get_list_episodes(api_url,'List_of_animated_series_episodes'):
            print(episode)
            try:
                html = fetchText(api_url+episode)

                episode_info = get_table(BeautifulSoup(html,"html.parser"))
                episode_info["Characters"] = get_characters(html,episode)
                episode_info["Plot"] = get_plot_from_episode(html,episode)
                episode_info["Major events"] = get_major_events(html, episode)

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

# Writes to a document unprocessed data of characters
def scrape_characters(num):
    with open("documents/characters.json","w") as json_file:
        final_document={}
        for character,character_code,first_appearance,role in get_list_characters(api_url,"List_of_animated_series_characters#Original_series"):
            print(character,character_code,first_appearance,role)
            try:
                html = fetchText(api_url+character_code)

                character_info = get_character_table_info(html,character_code)
                character_info["Character Code"] = character_code
                character_info["Role"] = role
                character_info["First Appearance"]=first_appearance
                character_info["Character"]=get_character_character(html,character_code)
                character_info["History"]=get_character_history(html,character_code)
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

def dataset_processing_characters(path_to_file):
    df = pd.read_json(path_to_file)
    df = df.transpose()
    # Extract 'First Appearance' from the nested dictionaries
    df["Age"]= df["Age"].apply((lambda string : re.search(r'\d+',string).group() if re.search(r'\d+', string) else pd.NA))
    print(df)
    return df
# Processes the dataset obtained from the series json file
# Arg path_to_file: string path to the json file
def dataset_processing_series(path_to_file):
    df = pd.read_json(path_to_file)
    df = df.transpose()
    # Extract 'Japan' and 'United States' dates from the nested dictionaries
    df['First broadcast Japan'] = df['First broadcast'].apply(lambda x: x.get('Japan') if isinstance(x, dict) else None)
    df['First broadcast United States'] = df['First broadcast'].apply(lambda x: x.get('United States') if isinstance(x, dict) else None)
    # Convert the extracted dates to datetime format
    df['First broadcast Japan'] = pd.to_datetime(df['First broadcast Japan'])
    df['First broadcast United States'] = pd.to_datetime(df['First broadcast United States'])

    # Extract the 'Characters' column and split it into 'Human Characters' and 'Pokemon Characters'
    df["Human Characters"] = df["Characters"].apply(lambda x: x.get("Humans") if isinstance(x, dict) else None)
    df["Pokemon Characters"] = df["Characters"].apply(lambda x: x.get("Pokemons") if isinstance(x, dict) else None)

    # Extract the 'English Themes' column and split it into 'English Themed Opening' and 'English Themed Ending'
    df["English Theme Opening"] = df["English themes"].apply(lambda x: x.get("Opening") if isinstance(x, dict) else None)
    df["English Theme Ending"] = df["English themes"].apply(lambda x: x.get("Ending") if isinstance(x, dict) else None)

    # Extract the 'Japanese Themes' column and split it into 'Japanese Themed Opening' and 'Japanese Themed Ending'
    df["Japanese Theme Opening"] = df["Japanese themes"].apply(lambda x: x.get("Opening") if isinstance(x, dict) else None)
    df["Japanese Theme Ending"] = df["Japanese themes"].apply(lambda x: x.get("Ending") if isinstance(x, dict) else None)

    # Extract the 'Credits' column and split it into many different columns with the respective credits
    for key in df["Credits"][0].keys():
        df[key] = df["Credits"].apply(lambda x: x.get(key) if isinstance(x, dict) else None)
    return df

    
#dataset_processing_series("documents/episodes.json")
dataset_processing_characters("documents/characters.json")
#scrape_characters(5)
