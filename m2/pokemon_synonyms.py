import pandas as pd
from fold_to_ascii import fold

pokemon_df = pd.read_json("data/docs/pokemons_final.json")

used_names = set()

with open("data/pokemon_synonyms.txt", "w") as file:
    for index, pokemon in pokemon_df.iterrows():
        name_l = str.lower(fold(pokemon["name"]))

        if name_l not in used_names:
            file.write(f"{name_l} => {name_l}, pokemon\n")
            used_names.add(name_l)