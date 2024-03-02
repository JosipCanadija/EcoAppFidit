from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
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

class GroupAssistantCreateView(CreateView):
    model = GroupAssistant
    form_class = GroupAssistantForm
    template_name = 'add_assistants.html'
    success_url = reverse_lazy('Eco:listAssistants')

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'add_user.html'
    success_url = reverse_lazy('Eco:listUsers')

class EcoActivityCreateView(CreateView):
    model = EcoActivity
    form_class = EcoActivityForm
    template_name = 'add_eco.html'
    success_url = reverse_lazy('Eco:listEco')

class OrganizerUpdateView(UpdateView):
    model = Organizer
    form_class = OrganizerForm
    template_name = 'update_organizers.html'
    success_url = reverse_lazy('Eco:listOrg')

class GroupAssistantUpdateView(UpdateView):
    model = GroupAssistant
    form_class = GroupAssistantForm
    template_name = 'update_assistants.html'
    success_url = reverse_lazy('Eco:listAssistants')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'update_user.html'
    success_url = reverse_lazy('Eco:listUsers')

class EcoActivityUpdateView(UpdateView):
    model = EcoActivity
    form_class = EcoActivityForm
    template_name = 'update_eco.html'
    success_url = reverse_lazy('Eco:listEco')

class OrganizerDeleteView(DeleteView):
    model = Organizer
    template_name = 'delete_organizers.html'
    success_url = reverse_lazy('Eco:listOrg')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = self.get_object()
        return context

class GroupAssistantDeleteView(DeleteView):
    model = GroupAssistant
    template_name = 'delete_assistants.html'
    success_url = reverse_lazy('Eco:listAssistants')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assistant'] = self.get_object()
        return context

class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('Eco:listUsers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.get_object()
        return context

class EcoActivityDeleteView(DeleteView):
    model = EcoActivity
    template_name = 'delete_eco.html'
    success_url = reverse_lazy('Eco:listEco')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eco_activity'] = self.get_object()
        return context
