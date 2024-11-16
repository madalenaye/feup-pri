import json 
import pandas as pd

def convert_to_iso(episodes):
    for episode in episodes:
        print(pd.to_datetime(episode["first broadcast japan"], unit='ms').isoformat())
        if(episode["first broadcast japan"]):
            episode["first broadcast japan"] = pd.to_datetime(episode["first broadcast japan"], unit='ms').isoformat()

        if(episode["first broadcast united states"]):
            episode["first broadcast united states"] = pd.to_datetime(episode["first broadcast united states"], unit='ms').isoformat()
    return episodes

def process_episodes(episodes):
    counter = 1
    for episode in episodes:
        episode["index"] = counter;
        episode["epcode"] = episode["id"];
        episode["title"] = episode["name"];
        del episode["name"];
        counter += 1;

    return episodes

with open('data/docs/new_episodes.json') as file:
    episodes = json.load(file)

episodes = process_episodes(convert_to_iso(episodes)) 

with open('data/docs/new_episodes.json', 'w') as file:
    json.dump(episodes, file, indent=4)