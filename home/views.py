from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'home/index.html', {
        "message": "This is dynamic message for basic crm app."
    })

def about(request):
    return HttpResponse("This is about page.")