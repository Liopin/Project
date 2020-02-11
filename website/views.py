from django.shortcuts import render
from .models import Service


# Create your views here.

def home(request):
    return render(request,'website/home_page/home.html')

def services(request):
    context = {
        'services' : Service.objects.all()
    }
    return render(request,'website/services_page/services.html', context)

def team(request):
    return render(request,'website/team_page/team.html')

def contact(request):
    return render(request,'website/contact_page/contact.html')
