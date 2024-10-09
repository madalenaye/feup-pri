import json
import re
from utils import set_default

def build_reverse_index(obj):
    for episode, episode_data in episodes.items():
        for human in episode_data["Characters"]["Humans"]:
            print(human)
            if (not human["code"]) or human["code"].replace("'", "%27") not in obj:
                continue
            character = obj[human["code"].replace("'", "%27")]
            if "Appearances" in character:
                character["Appearances"].add(episode)
            else:
                character["Appearances"] = set([episode])

def get_correlations():
    pattern = re.compile("(main|Main|recurring|Recurring)")
    filtered_characters = {}
    for character, character_data in characters.items():
        if pattern.search(character_data["Role"]):
            filtered_characters[character] = character_data

    build_reverse_index(filtered_characters)
    print(json.dumps(filtered_characters, indent=2, default=set_default))

with open('documents/episodes.json', 'r') as file:
    episodes = json.load(file)

with open('documents/characters.json', 'r') as file:
    characters = json.load(file)

get_correlations()