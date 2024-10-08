from characters_scraper import *
from series_scraper import * 
from utils import *
import pandas as pd 
import json
import re
import matplotlib.pyplot as plt 
from wordcloud import WordCloud
import traceback
# Writes to a document unprocessed data of episodes
def scrape_episodes(num):
    with open("documents/episodes.json","w") as json_file:
        final_document={}
        for episode in get_list_episodes(api_url,"List_of_animated_series_episodes"):
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
                traceback.print_exc()
                continue
            finally:
                num -= 1
                if num <= 0:
                    break
        json.dump(final_document,json_file)

def extract_age(string):
    if isinstance(string, list):
        text = ""
        for s in string:
            text += s
        age = re.search(r'\d+',text).group()
        if age:
            return int(age)
        else:
            return pd.NA
    else:
        age = re.search(r'\d+',string).group()
        if age:
            return int(age)
        else:
            return pd.NA

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
    # Extract 'Age' from the string or list of strings
    df["Age"]= df["Age"].apply(extract_age)
    # Merge 'Animated debut' and 'Debut' columns since they mean the same thing
    df["Debut"] = df["Animated debut"].fillna(df["Debut"])
    df.drop(columns=["Animated debut"],inplace=True)
    # Drop unnecessary columns
    df.drop(columns=["Game counterpart","Manga counterpart(s)","Manga series","Games","Generation","Counterpart(s)"],inplace=True)
    # Fill NaN values with 'Unknown
    df.fillna(value="Unknown",inplace=True) 
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

    # Extract the 'English Themes' column and split it into 'English Theme Opening' and 'English Theme Ending'
    df["English Theme Opening"] = df["English themes"].apply(lambda x: x.get("Opening") if isinstance(x, dict) else None)
    df["English Theme Ending"] = df["English themes"].apply(lambda x: x.get("Ending") if isinstance(x, dict) else None)

    # Extract the 'Japanese Themes' column and split it into 'Japanese Themed Opening' and 'Japanese Themed Ending'
    df["Japanese Theme Opening"] = df["Japanese themes"].apply(lambda x: x.get("Opening") if isinstance(x, dict) else None)
    df["Japanese Theme Ending"] = df["Japanese themes"].apply(lambda x: x.get("Ending") if isinstance(x, dict) else None)

    # Extract the 'Credits' column and split it into many different columns with the respective credits
    for key in df["Credits"][0].keys():
        df[key] = df["Credits"].apply(lambda x: x.get(key) if isinstance(x, dict) else None)
    # Fill NaN values with 'Unknown'
    df.fillna(value="Unknown",inplace=True)
    return df

 # Set display options to show all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Plot word cloud:
#arg df: dataframe
def plot_word_cloud(df,column):
    all_plot = ' '.join(df[column].astype(str))  
    
    # Create a word cloud
    wordcloud = WordCloud(width = 800, height = 800, 
                    background_color ='white', 
                    ).generate(all_plot)
    plt.figure(figsize = (10, 10), facecolor = None)
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.axis("off")
    plt.show()

#print(dataset_processing_series("documents/episodes.json"))
#print(dataset_processing_characters("documents/characters.json"))
scrape_episodes(274)
#plot_word_cloud(dataset_processing_series("documents/episodes.json"),"Plot")
