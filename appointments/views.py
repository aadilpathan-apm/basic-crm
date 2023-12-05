from django.shortcuts import render

# Create your views here.
def index(request):# URL Dispatchise.
    return render(request, 'appointments/index.html', {
        "message": "This is appointments page."
    })