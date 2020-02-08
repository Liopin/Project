from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='website-home'),
    path('services/', views.services, name='website-services'),
    path('équipe/', views.team, name='website-team'),
    path('contact/', views.contact, name='website-contact'),
    
]