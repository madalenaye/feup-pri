import json

def find_character(code, characters):
    for character in characters:
        if character["Character Code"] == code:
            return character
        
    return None

def merge_single_human(human, characters):
    to_keep = ["Gender", "Debut", "Character", "English voice actor", "Japanese voice actor"]

    full_human = find_character(human["code"], characters)
    if (full_human is None):
        return human

    for attr in to_keep:
        #print(full_human[attr])
        human[attr] = full_human[attr]

    return human

def merge_humans(episodes, characters):
    for episode_data in episodes:
        episode_data["human characters"] = list(map(lambda x: merge_single_human(x, characters), episode_data["human characters"]))

with open("data/episodes_final.json", "r") as episode_file, open("data/characters_final.json") as character_file:
    episodes = json.load(episode_file)
    characters = json.load(character_file)

merge_humans(episodes, characters)
with open("new_episodes.json", "w") as new_file:
    json.dump(episodes, new_file, indent=4)