from django.shortcuts import render, HttpResponse

def index(request):# URL Dispatchise.
    return render(request, 'task/index.html', {
        "message": "This is task page."
    })