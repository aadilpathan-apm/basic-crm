from django.shortcuts import render

# Create your views here.
def index(request):# URL Dispatchise.
    return render(request, 'customers/index.html', {
        "message": "This is customers page."
    })