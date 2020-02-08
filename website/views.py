from django.shortcuts import render
from django. http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<h1>home<h1>')

def services(request):
    return HttpResponse('<h1>services<h1>')

def team(request):
    return HttpResponse('<h1>equipes<h1>')

def contact(request):
    return HttpResponse('<h1>contact<h1>')
