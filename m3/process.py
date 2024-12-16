import json 
import pandas as pd
import urllib.request
import urllib.parse

def convert_to_iso(episodes):
    for episode in episodes:
        print(pd.to_datetime(episode["first_broadcast_japan"], unit='ms').isoformat())
        if(episode["first_broadcast_japan"]):
            episode["first_broadcast_japan"] = pd.to_datetime(episode["first_broadcast_japan"], unit='ms').isoformat()

        if(episode["first_broadcast_united_states"]):
            episode["first_broadcast_united_states"] = pd.to_datetime(episode["first_broadcast_united_states"], unit='ms').isoformat()
    return episodes

def fetchImage(title):
    encoded_title = urllib.parse.quote(title)
    url = f"https://bulbapedia.bulbagarden.net/w/api.php?action=query&titles={encoded_title}&redirects&prop=pageimages&format=json&pithumbsize=10000"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        pageid, pageContent = list(json.load(url)["query"]["pages"].items())[0]
        print(pageContent);
        return pageContent["thumbnail"]["source"];
def addImageEp(document):
    return fetchImage(document["id"])

    return human_characters;
def process_episodes(episodes):
    counter = 1
    for episode in episodes:
        episode["index"] = counter
        episode["epcode"] = episode["id"]
        episode["title"] = episode["name"]
        episode["title_query"] = episode["title"]
        episode["major_event_count"] = len(episode["major_events"])
        del episode["name"]
        episode["paragraphs"] = []
        plot_len = len(episode["plot"])
        last_paragraph = 0
        for idx, char in enumerate(episode["plot"]):
            if char == '.' and idx + 1 < plot_len and episode["plot"][idx + 1] != ' ':
                episode["paragraphs"].append(episode["plot"][last_paragraph:(idx+1)])
                last_paragraph = idx+1
        episode["paragraphs"].append(episode["plot"][last_paragraph:len(episode["plot"])])
        episode["image"] = addImageEp(episode);

        counter += 1

    return episodes

with open('data/docs/new_episodes.json') as file:
    episodes = json.load(file)

episodes = process_episodes(convert_to_iso(episodes)) 

with open('data/docs/new_episodes.json', 'w') as file:
    json.dump(episodes, file, indent=4)



