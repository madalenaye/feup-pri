import json
import sys
import requests
import os

mlt = {
    "results": "./data/docs/related_docs.json",
    "parameters": {
        "mlt.fl": "plot, title, major_events",
        "mlt.mintf": 2,
        "mlt.mindf": 6,
        "mlt.qf": "plot^8 title^2 major_events^5",
        "sort": "score desc",
        "rows": 5,
        "fl": "id, score,major_events,image, title , plot,paragraphs,human_characters,first_broadcast_japan,first_broadcast_united_states,english_theme_opening,english_theme_ending,japanese_theme_opening,japanese_theme_ending,animation,screenplay,storyboard,assistant_director,animation_directors"
    }
}

def fetch_solr_results(id, solr_uri, collection):
    uri = f"{solr_uri}/{collection}/mlt"
    
    params = {
        **mlt["parameters"],
        "q": f"id:{id}"
    }
    try:
        response = requests.get(uri, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error querying Solr: {e}")
        sys.exit(1)
    
    docs = response.json().get("response", {}).get("docs", [])

    return docs

if __name__ == "__main__":
    with open("./data/docs/new_episodes.json", "r") as file:
        episodes = json.load(file)
    
    
    results = []
        
    for episode in episodes:
        result = fetch_solr_results(episode, "http://localhost:8983/solr", "episodes")
        results.append(result)
    
    with open(mlt["results"], "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)
    print("Done!")