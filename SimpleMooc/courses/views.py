from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.


def index(request):
    courses = Course.objects.all()
    path = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, path, context)


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    path = 'courses/details.html'
    context = {
        'course': course
    }
    return render(request, path, context)
