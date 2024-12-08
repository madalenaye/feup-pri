import sys
import json
from sentence_transformers import SentenceTransformer

# Load the SentenceTransformer model
model = SentenceTransformer('all-mpnet-base-v2')

def get_embedding(text):
    # The model.encode() method already returns a list of floats
    return model.encode(text, convert_to_tensor=False).tolist()

if __name__ == "__main__":
    # Read JSON from STDIN
    data = json.load(sys.stdin)
    print("data loaded")

    # Update each document in the JSON data
    for document in data:
        print("episode")
        print(document["id"])
        # Extract fields if they exist, otherwise default to empty strings
        #title = document.get("title", "")
        plot = document.get("paragraphs", [])
        major_events = document.get("major_events", [])

        document["embeddings"] = []
        for paragraph in plot:
            document["embeddings"].append({"vector": get_embedding(paragraph)})
        for event in major_events:
            document["embeddings"].append({"vector": get_embedding(event)})



        #combined_text = title + " " + plot + " " + ' '.join(major_events)
        #document["vector"] = get_embedding(combined_text)

    # Output updated JSON to STDOUT
    #json.dump(data, sys.stdout, indent=4, ensure_ascii=False)
    with open('data/docs/chunked_episodes_2.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)