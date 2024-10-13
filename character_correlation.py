import json
import re
from utils import set_default
import pandas as pd

def build_reverse_index(obj):
    for episode, episode_data in episodes.items():
        for human in episode_data["Characters"]["Humans"]:
            if (not human["code"]) or human["code"].replace("'", "%27") not in obj:
                continue
            character = obj[human["code"].replace("'", "%27")]
            if "Appearances" in character:
                character["Appearances"].add(episode)
            else:
                character["Appearances"] = set([episode])

def get_correlations(file):
    pattern = re.compile("(main|Main|recurring|Recurring)")
    filtered_characters = {}
    for character, character_data in characters.items():
        if pattern.search(character_data["Role"]):
            filtered_characters[character] = character_data

    build_reverse_index(filtered_characters)

    char_list = list(filtered_characters.items())
    char_len = len(char_list)
    pairs = []
    for i in range(char_len-1):
        for j in range(i+1, char_len):
            if "Appearances" not in char_list[i][1] or "Appearances" not in char_list[j][1]:
                continue

            union = len(char_list[i][1]["Appearances"] | char_list[j][1]["Appearances"])
            intersection = len(char_list[i][1]["Appearances"] & char_list[j][1]["Appearances"])
            pairs.append((char_list[i][0], char_list[j][0], intersection/union))

    df = pd.DataFrame(pairs, columns = ["Character 1", "Character 2", "Correlation"])
    df = df.sort_values(by="Correlation", ascending=False).reset_index()
    df.to_json(file, orient="index")

with open('documents/episodes.json', 'r') as file:
    episodes = json.load(file)

with open('documents/characters.json', 'r') as file:
    characters = json.load(file)