from django.shortcuts import render

# Create your views here.
def index(request):# URL Dispatchise.
    return render(request, 'notes/index.html', {
        "message": "This is notes page."
    })