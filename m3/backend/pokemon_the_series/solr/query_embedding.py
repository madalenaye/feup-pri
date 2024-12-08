import json
import sys
import requests
from sentence_transformers import SentenceTransformer

def text_to_embedding(text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(text, convert_to_tensor=False).tolist()
    
    # Convert the embedding to the expected format
    embedding_str = "[" + ",".join(map(str, embedding)) + "]"
    return embedding_str

def solr_knn_query(endpoint, collection, filename):
    url = f"{endpoint}/{collection}/select"

    try:
        query_params = json.load(open(filename))
    except FileNotFoundError:
        print(f"Error: Query file {filename} not found.")
        sys.exit(1)

    #data = {
    #    "q": f"{{!knn f=vector topK=30}}{embedding}",
    #    "fl": "id,title,score",
    #    "rows": 30,
    #    "wt": "json"
    #}
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    embedding = text_to_embedding(query_params["query"])

    query_params["params"]["rqq"] = f"{{!knn f=vector topK=100}}{embedding}"
    
    response = requests.post(url, json=query_params)
    response.raise_for_status()
    return response.json()

def display_results(results):
    docs = results.get("response", {}).get("docs", [])
    if not docs:
        print("No results found.")
        return

    for doc in docs:
        print(f"* {doc.get('id')} {doc.get('title')} [score: {doc.get('score'):.2f}]")

def make_query(filename):
    solr_endpoint = "http://localhost:8983/solr"
    collection = "episodes"
    
    #uery_text = input("Enter your query: ")
    #embedding = text_to_embedding(query_text)

    try:
        results = solr_knn_query(solr_endpoint, collection, filename)
        display_results(results)
    except requests.HTTPError as e:
        print(f"Error {e.response.status_code}: {e.response.text}")


