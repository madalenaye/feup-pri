
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .solr.query_embedding import make_query;

@csrf_exempt
def query(request):
    if request.method == 'POST':
        try:
            make_query("chunked_episodes.json")
            return HttpResponse(f"Received query: {query}")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
    