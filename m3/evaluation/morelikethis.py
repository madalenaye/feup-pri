import spacy
import json

nlp = spacy.load("en_core_web_sm")
mlt_results = './data/docs/related_docs.json'
eval_results = './evaluation/mlt/evaluation.json'
new_episodes = './data/docs/new_episodes.json'


def calc_similarity(episode_id, related_episodes):
    episode_plot = get_plot(episode_id)
    similarities = []
    for i in related_episodes:
        related_plot = get_plot(i['id'])
        doc1 = nlp(episode_plot)
        doc2 = nlp(related_plot)
        similarity = round(doc1.similarity(doc2), 3)
        print(similarity)
        similarities.append(similarity)
    return similarities
        
def get_plot(episode_id):
    with open(new_episodes, "r") as file:
        episodes = json.load(file)
        file.close()
    for i in episodes:
        if i['id'] == episode_id:
            return i['plot']
    return None
    
def main():

    results = []
    with open(mlt_results, "r") as file:
        results = json.load(file)
        file.close()
    evaluation = []
    for i in results:
        episode = i['id']
        related_episodes = i['related']
        similarities = calc_similarity(episode, related_episodes)
        r = {"id": episode, "similarities": similarities}
        evaluation.append(r)
    
    with open(eval_results, "w") as file:
        json.dump(evaluation, file)
        file.close()

if __name__ == "__main__":
    main()