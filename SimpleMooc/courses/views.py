from django.shortcuts import render

# Create your views here.
def courses(request):
    path = 'courses/courses.html'
    return render(request, path)
