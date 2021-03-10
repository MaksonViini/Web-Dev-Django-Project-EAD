from django.contrib import admin
from django.urls import path
from SimpleMooc.courses import views

urlpatterns = [
    path('cursos/', views.index, name='index')
]
