from django.shortcuts import render

# Create your views here.
def index(request):
    path = 'courses/index.html'
    return render(request, path)
