
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .solr import query_pure_semantic;
from .solr import query_solr;
def queryEpisodesPureSemantic(request):
    queryInfo = {
        "query": "{!parent which=\"plot:*\" score=max}{!knn f=vector topK=500}",
        "fields": "id, score, title , plot",
        "limit": 30,
        "querytext": "",
        "params": {
        }
    }
    if request.method == 'POST':
        try:
            requestBody = json.loads(request.body)
            query= requestBody['query']
            queryInfo['querytext'] = query
            results = query_pure_semantic.fetch_solr_results(queryInfo, "http://localhost:8983/solr", "episodes")
            return HttpResponse(json.dumps(results), content_type="application/json")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)

def queryPokemons(request):
    queryInfo = {
    "query":"",
    "filter": "{!collapse field='image'}",
    "fields": "id, score,pokedex_entry, name, biology,blurb,image",
    "limit": 30,
    "params": {
      "defType": "edismax",
      "q.op": "OR",
      "qf": "biology^10 blurb^2"
    }
    }
    if request.method =='POST':
        try:
            requestBody = json.loads(request.body)
            query= requestBody['query']
            queryInfo['query'] = query
            results = query_solr.fetch_solr_results(queryInfo, "http://localhost:8983/solr", "episodes")
            print("results are :", results);
            return HttpResponse(json.dumps(results), content_type="application/json")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
  