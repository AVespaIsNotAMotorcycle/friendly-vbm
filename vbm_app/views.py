from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

# Create your views here.

def index(request):
    """The home page for VBM Buster."""
    return render(request, 'vbm_app/index.html')
    
def bruteURI(request):
    """Main page for brute forcing URIs."""
    print('LOOK HERE', request.GET)
    print(request.GET['words'])
    words = json.loads(request.GET['words'])
    results = {}
    for word in words:
        results[word] = requests.get('https://' + request.GET['domain'] + '/' + word).status_code
    return JsonResponse(results)

def bruteReqs(request):
    """Main page for brute forcing types of requests."""
    return render(request, 'vbm_app/bruteReqs.html')