
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .solr import query_pure_semantic;

@csrf_exempt
def query(request):
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