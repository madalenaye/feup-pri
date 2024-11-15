import nltk
from nltk.corpus import wordnet

nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('wordnet', quiet=True)

words = ["win", "lose", "victory", "defeat", "battle", "friend", "anger", "angry", "sad", "catch", "group", "help", "tries", "run"]

for word in words:
    synonyms = set()
    for synonym in wordnet.synsets(word):
        for name in synonym.lemma_names():
            synonyms.add(name)
    print(list(synonyms))