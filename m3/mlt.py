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
        "sort": "score desc",
        "rows": 5
    }
}

def fetch_solr_results(episode, solr_uri, collection):
    uri = f"{solr_uri}/{collection}/mlt"
    
    params = {
        **mlt["parameters"],
        "q": f"id:{episode['id']}"
    }
    try:
        response = requests.get(uri, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error querying Solr: {e}")
        sys.exit(1)
    
    docs = response.json().get("response", {}).get("docs", [])
    
    if len(docs) > 0:
        if os.path.exists(mlt["results"]):
            with open(mlt["results"], "r", encoding="utf-8") as file:
                results = json.load(file)
        else:
            results = []
        
        results.append({
            "id": episode["id"],
            "related": [{"id": docs[i]["id"]} for i in range(len(docs))]
        })
        with open(mlt["results"], "w", encoding="utf-8") as file:
            json.dump(results, file, indent=2)
    
    return docs

if __name__ == "__main__":
    with open("./data/docs/new_episodes.json", "r") as file:
        episodes = json.load(file)
    
    for episode in episodes:
        fetch_solr_results(episode, "http://localhost:8983/solr", "episodes")
    
    print("Done!")