from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .solr import query_pure_semantic;
from .solr import query_solr;
from .solr import query_rerank;
import urllib.request
import urllib.parse


def queryEpisodesPureSemantic(request):
    queryInfo = {
        "query": "{!parent which=\"plot:*\" score=max}{!knn f=vector topK=500}",
        "fields": "id, score,major_events,image, title , plot,paragraphs,human_characters,first_broadcast_japan,first_broadcast_united_states,english_theme_opening,english_theme_ending,japanese_theme_opening,japanese_theme_ending,animation,screenplay,storyboard,assistant_director,animation_directors",
        "limit": 5000,
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
            results = [document for document in results["response"]["docs"]]

            print(results[0])
            return HttpResponse(json.dumps(results), content_type="application/json")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)

def queryPokemons(request):
    queryInfo = {
    "query":"",
    "filter": "{!collapse field='image'}",
    "fields": "id, score,pokedex_entry, name, biology,blurb,image,abilities ,types",
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
            results = [doc for doc in results["response"]["docs"]]
            return HttpResponse(json.dumps(results), content_type="application/json")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
  
def queryEpRerank(request):
    queryInfo= {
        "query": "",
        "filter": "-_nest_path_:*",
        "fields": "id, score,major_events,image, title , plot,paragraphs,human_characters,first_broadcast_japan,first_broadcast_united_states,english_theme_opening,english_theme_ending,japanese_theme_opening,japanese_theme_ending,animation,screenplay,storyboard,assistant_director,animation_directors",
        "limit": 30,
        "params": {
        "defType": "edismax",
        "q.op": "AND",
        "qf": "title_query^7 major_events^10 plot^4",
        "pf": "plot^25 major_events^25",
        "ps": "6",
        "rq": "{!rerank reRankQuery=$rqq reRankWeight=4 reRankDocs=30}"
        }
    }
    if request.method =='POST':
        try:
            requestBody = json.loads(request.body)
            query= requestBody['query']
            queryInfo['query'] = query
            
            results = query_rerank.fetch_solr_results(queryInfo, "http://localhost:8983/solr", "episodes")
            results = results["response"]["docs"]
            
            
            return HttpResponse(json.dumps(results), content_type="application/json")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)