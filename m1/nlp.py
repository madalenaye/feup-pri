import spacy
import json
from spacy import displacy
from collections import Counter

with open('documents/episodes.json', 'r') as file:
    data = json.load(file)

nlp = spacy.load("en_core_web_md")

doc = nlp(data["EP004"]["Plot"])

ents = Counter()

for ent in doc.ents:
    ents[f"{ent.label_}:{ent.text}"] += 1

for key, val in ents.items():
    print(val, key, sep="\t")

with open('test.svg', 'w') as file:
    svg = displacy.serve(doc, style="ent", host="localhost")