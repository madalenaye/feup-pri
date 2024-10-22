import json

# Load your original JSON
pokemon_input_file = '/home/tomasvicente3/files/cadeiras/pri/feup-pri/m1/documents/pokemons_final.json'
pokemon_output_file = '/home/tomasvicente3/files/cadeiras/pri/feup-pri/m2/data/pokemons.json'

# Function to transform the original JSON structure to Solr format
def transform_to_solr_format(pokemon_data):
    solr_data = {"add": []}

    for pokemon_name, pokemon_info in pokemon_data.items():
        # Extract data from the original structure
        pokedex_entry = pokemon_info.get("Pokedex Entry", "")
        pokemon_page = pokemon_info.get("Pokemon Page", "")
        types = pokemon_info.get("Types", [])
        blurb = pokemon_info.get("Blurb", "")
        biology = pokemon_info.get("Biology", "")
        image = pokemon_info.get("Image", "")
        abilities = pokemon_info.get("Abilities", [])

        # Create a Solr document for each Pokemon
        solr_doc = {
            "id": pokedex_entry.strip("#"),  # Strip the '#' from the Pokedex Entry
            "name": pokemon_name,
            "page": pokemon_page,
            "types": types,
            "blurb": blurb,
            "biology": biology,
            "image": image,
            "abilities": abilities
        }

        # Add the document to the Solr data structure
        solr_data["add"].append(solr_doc)

    return solr_data

# Load the input JSON file
with open(pokemon_input_file, 'r', encoding='utf-8') as f:
    pokemon_data = json.load(f)

# Transform the data to Solr format
solr_formatted_data = transform_to_solr_format(pokemon_data)

# Save the transformed data to a new JSON file
with open(pokemon_output_file, 'w', encoding='utf-8') as f:
    json.dump(solr_formatted_data, f, indent=2, ensure_ascii=False)

print(f"Transformation complete! Output saved to {pokemon_output_file}")
