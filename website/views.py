from django.shortcuts import render
from django. http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'website/home.html')

def services(request):
    return render(request,'website/services.html')

def team(request):
    return render(request,'website/team.html')

def contact(request):
    return render(request,'website/contact.html')
