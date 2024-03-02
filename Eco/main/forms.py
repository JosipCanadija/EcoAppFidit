from django import forms
from .models import Organizer, EcoActivity, User, GroupAssistant


class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['org_name', 'org_lastname', 'org_contact', 'org_companyID']


class EcoActivityForm(forms.ModelForm):
    class Meta:
        model = EcoActivity
        fields = ['eco_name', 'eco_summary', 'eco_date', 'eco_author']
        widgets = {
            'eco_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_lastname', 'user_id', 'user_activ']


class GroupAssistantForm(forms.ModelForm):
    class Meta:
        model = GroupAssistant
        fields = ['mentor', 'user', 'ass_task', 'ass_done']
