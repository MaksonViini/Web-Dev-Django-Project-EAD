from django.contrib import admin
from django.urls import path
from SimpleMooc.courses import views

urlpatterns = [
    path('', views.courses, name='index')
]
