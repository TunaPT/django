#  hello/urls.py

from django.urls import path
from django.shortcuts import render
from . import views

app_name = "portfolio"

urlpatterns = [
    path('home', views.home_view, name='home')
]