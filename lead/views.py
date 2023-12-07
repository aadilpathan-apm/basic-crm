from django.shortcuts import render

def index(request):# URL Dispatchise.
    return render(request, 'lead/index.html', {})