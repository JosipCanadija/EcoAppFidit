from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import *

# Create your views here.

class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base_generic.html')

def landing_page(request):
    return render(request, 'base_generic.html')

class OrganizerListView(ListView):
    model = Organizer
    template_name = 'list_organizers.html'
    context_object_name = 'organizers'

class EcoActivityListView(ListView):
    model = EcoActivity
    template_name = 'list_eco.html'
    context_object_name = 'eco'

class UserListView(ListView):
    model = User
    template_name = 'list_user.html'
    context_object_name = 'users'

class GroupAssistantListView(ListView):
    model = GroupAssistant
    template_name = 'list_assistants.html'
    context_object_name = 'groups'