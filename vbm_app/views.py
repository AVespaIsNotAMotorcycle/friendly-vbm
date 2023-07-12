from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for VBM Buster."""
    return render(request, 'vbm_app/index.html')
    
def bruteURI(request):
    """Main page for brute forcing URIs."""
    return render(request, 'vbm_app/bruteURI.html')

def bruteReqs(request):
    """Main page for brute forcing types of requests."""
    return render(request, 'vbm_app/bruteReqs.html')