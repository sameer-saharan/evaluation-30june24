from django.shortcuts import render, get_object_or_404, redirect
from .models import Services, ServiceUser
from django.views.generic import ListView, DetailView

class UserView(ListView):
    model = ServiceUser
    template_name = 'index.html'
    context_object_name = 'users' 

def showUserDetails(request, id): 
    user = get_object_or_404(ServiceUser, pk=id)
    service = user.service.all()
    return render(request, 'users.html', {"user": user, "service": service})

class ServiceView(ListView): 
    model = Services
    template_name = 'index2.html'
    context_object_name = 'services'

def showServiceDetails(request, type): 
    service = get_object_or_404(Services, type=type)
    users = ServiceUser.objects.filter(service=service)
    return render(request, 'services.html', {"service": service, "users": users})