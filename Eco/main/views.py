from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import *

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

class OrganizerCreateView(CreateView):
    model = Organizer
    form_class = OrganizerForm
    template_name = 'add_organizers.html'
    success_url = reverse_lazy('Eco:listOrg')