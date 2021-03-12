from django.contrib import admin
from django.urls import path, re_path
from SimpleMooc.courses import views

urlpatterns = [
    path('cursos/', views.index, name='index'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.details, name='details')
]
