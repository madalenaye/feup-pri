import json 
import pandas as pd

def convert_to_iso(episodes):
    for episode in episodes:
        print(pd.to_datetime(episode["first_broadcast_japan"], unit='ms').isoformat())
        if(episode["first_broadcast_japan"]):
            episode["first_broadcast_japan"] = pd.to_datetime(episode["first_broadcast_japan"], unit='ms').isoformat()

        if(episode["first_broadcast_united_states"]):
            episode["first_broadcast_united_states"] = pd.to_datetime(episode["first_broadcast_united_states"], unit='ms').isoformat()
    return episodes

def process_episodes(episodes):
    counter = 1
    for episode in episodes:
        episode["index"] = counter
        episode["epcode"] = episode["id"]
        episode["title"] = episode["name"]
        episode["title_query"] = episode["title"]
        del episode["name"]
        counter += 1

    return episodes

with open('data/docs/new_episodes.json') as file:
    episodes = json.load(file)

episodes = process_episodes(convert_to_iso(episodes)) 

with open('data/docs/new_episodes.json', 'w') as file:
    json.dump(episodes, file, indent=4)