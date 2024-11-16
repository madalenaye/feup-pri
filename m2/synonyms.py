import nltk
from nltk.corpus import wordnet
import pandas as pd

nltk.download('averaged_perceptron_tagger_eng', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)

pokemon_df = pd.read_json("data/docs/pokemons_final.json")
biologies = [pokemon["Biology"] for index, pokemon in pokemon_df.iterrows()]

used_words = set()
syn_list = []

for biology in biologies:
    adjectives = [word.lower() for word, pos in nltk.pos_tag(nltk.word_tokenize(biology)) if pos in ['JJ', 'JJR', 'JJS'] and word.lower() not in used_words]

    for adj in adjectives:
        syns = [adj]
        for syn in wordnet.synsets(adj):
            for lemma in syn.lemma_names():
                if lemma.lower() != adj:
                    syns.append(lemma)
        used_words.add(adj)
        if len(syns) > 2:
            syn_list.append(syns)

with open("data/synonyms.txt", "w") as synfile:
    for l in syn_list:
        synfile.write(" ,".join(l) + '\n')

