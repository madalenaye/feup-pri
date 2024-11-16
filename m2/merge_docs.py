import json

def find_character(code, characters):
    for character in characters:
        if character["character_code"] == code:
            return character
        
    return None

def merge_single_human(human, characters):
    to_keep = ["gender", "debut", "character", "english_voice_actor", "japanese_voice_actor"]

    full_human = find_character(human["code"], characters)
    if (full_human is None):
        return human

    for attr in to_keep:
        #print(full_human[attr])
        human[attr] = full_human[attr]

    return human

def merge_humans(episodes, characters):
    for episode_data in episodes:
        episode_data["human_characters"] = list(map(lambda x: merge_single_human(x, characters), episode_data["human_characters"]))

def find_pokemon(code,pokemons):
    for pokemon in pokemons:
        if pokemon["pokemon_page"] == code:
            return pokemon
    return None    
def merge_single_pokemon(pokemon, pokemons):
    all_pokemon = find_pokemon(pokemon["code"], pokemons)
    if(all_pokemon is None):
        return pokemon
    for attr in all_pokemon.keys():
        pokemon[attr] = all_pokemon[attr]
    return pokemon
def merge_pokemons(episodes,pokemon):
    for episode_data in episodes:
        episode_data["pokemon_characters"] = list(map(lambda x: merge_single_pokemon(x, pokemon), episode_data["pokemon_characters"]))
with open("data/docs/episodes_final.json", "r") as episode_file, open("data/docs/characters_final.json") as character_file,open("data/docs/pokemons_final.json") as pokemon_file:
    episodes = json.load(episode_file)
    characters = json.load(character_file)
    pokemons = json.load(pokemon_file)

merge_humans(episodes, characters)
merge_pokemons(episodes, pokemons)
with open("data/docs/new_episodes.json", "w") as new_file:
    json.dump(episodes, new_file, indent=4)
