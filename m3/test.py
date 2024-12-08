import requests

rep = requests.post("https://superhero-05-03-150699885662.europe-west1.run.app/generate", json={"code": "wewo", "diagramType": "Activity Diagram"})
#rep.raise_for_status()
print(rep.json())