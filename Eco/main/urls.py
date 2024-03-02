from django.urls import path
from . import views

app_name = 'Eco'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('listOrg/', views.OrganizerListView.as_view(), name='listOrg'),
    path('listEco/', views.EcoActivityListView.as_view(), name='listEco'),
    path('listUsers/', views.UserListView.as_view(), name='listUsers'),
    path('listAssistants/', views.GroupAssistantListView.as_view(), name='listAssistants'),
    path('addOrganizers/', views.OrganizerCreateView.as_view(), name='addOrganizers'),
    path('addEco/', views.EcoActivityCreateView.as_view(), name='addEco'),
    path('addUser/', views.UserCreateView.as_view(), name='addUser'),
    path('addAssistant/', views.GroupAssistantCreateView.as_view(), name='addAssistant'),
    path('updateAssistant/<int:pk>/', views.GroupAssistantUpdateView.as_view(), name='updateAssistant'),
    path('deleteAssistant/<int:pk>/', views.GroupAssistantDeleteView.as_view(), name='deleteAssistant'),
    path('updateUser/<int:pk>/', views.UserUpdateView.as_view(), name='updateUser'),
    path('deleteUser/<int:pk>/', views.UserDeleteView.as_view(), name='deleteUser'),
    path('updateEco/<int:pk>/', views.EcoActivityUpdateView.as_view(), name='updateEco'),
    path('deleteEco/<int:pk>/', views.EcoActivityDeleteView.as_view(), name='deleteEco'),
    path('updateOrganizers/<int:pk>/', views.OrganizerUpdateView.as_view(), name='updateOrganizers'),
    path('deleteOrganizers/<int:pk>/', views.OrganizerDeleteView.as_view(), name='deleteOrganizers'),

]