from django.shortcuts import render

# Create your views here.
def index(request):# URL Dispatchise.
    return render(request, 'mettings/index.html', {
        "message": "This is mettings page."
    })