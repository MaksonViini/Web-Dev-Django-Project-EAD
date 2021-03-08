from django.contrib import admin
from django.urls import path
from SimpleMooc.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact')
]
