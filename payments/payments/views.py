from django.shortcuts import render, get_object_or_404, redirect
from .models import Services, ServiceUser, Subscription
from django.views.generic import ListView, CreateView
from .forms import CreateSubcriptionForm, SubscriptionForm

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


def createSubscription(request): 
    if request.method == 'POST': 
        form = CreateSubcriptionForm(request.POST)
        if form.is_valid(): 
            form.save()

    else: 
        form = CreateSubcriptionForm() 

    return render(request, 'create.html', {"form": form})

class SubscriptionCreateView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'subscription.html'
    success_url = '/subscription/'

    def form_valid(self, form):
        return super().form_valid(form)