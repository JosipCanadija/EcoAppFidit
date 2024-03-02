from django.urls import path
from . import views

app_name = 'Eco'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('listOrg/', views.OrganizerListView.as_view(), name='listOrg'),
    path('listEco/', views.EcoActivityListView.as_view(), name='listEco'),
    path('listUsers/', views.UserListView.as_view(), name='listUsers'),
    path('listAssistants/', views.GroupAssistantListView.as_view(), name='listAssistants'),

]