import json 
import pandas as pd
import urllib.request
import urllib.parse

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
    for episode in episodes:
        episode["image"] = addImageEp(episode);
    return episodes
with open('data/docs/chunked_episodes_2.json',"r") as file:
    chunked_eps = json.load(file);
chunked_eps = process_episodes(chunked_eps);

