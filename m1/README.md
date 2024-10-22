### Data pipeline usage

```bash
python3 main.py <FLAGS>
```

## Options:

- ```--pokemon-file```: Choose where to store character data (default: ```documents/characters.json```)
- ```--episode-file```: Choose where to store episode data (default: ```documents/episodes.json```)
- ```--pokemon-file```: Choose where to store Pokémon data (default: ```documents/pokemons.json```)
- ```--scrape-characters```: Scrape character data
- ```--scrape-pokemon```: Scrape Pokémon data
- ```--scrape-episodes```: Scrape episode data
- ```-b/--broadcast-delay```, ```-w/--word-count```, ```-m/--major-events```, ```-o/--character-occurences```, ```-p/--pokemon-types```, ```-c/--word-cloud```: If each flag is present, the corresponding graph will be created. A filename can be specified, but is optional, as they all have default values

## Installing requirements:

```bash
pip install -r requirements.txt
```

# Note:
Processed data is stored with the same name as the unprocessed data, postfixed with _final. For example, ```documents/episodes.json``` becomes ```documents/episodes_final.json```.
