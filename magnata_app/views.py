from django.shortcuts import render

def index(request):
    return render(request, 'magnata_app/index.html')
