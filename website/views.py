from django.shortcuts import render
from django.template import Context, Template
from django. http import HttpResponse

services = [
    {
        'title': 'Service 1',
        'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    },
    {
        'title': 'Service 2',
        'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    }
]


# Create your views here.

def home(request):
    return render(request,'website/home_page/home.html')

def services(request):
    context = {
        'services' : services
    }
    return render(request,'website/services_page/services.html', context)

def team(request):
    return render(request,'website/team_page/team.html')

def contact(request):
    return render(request,'website/contact_page/contact.html')
