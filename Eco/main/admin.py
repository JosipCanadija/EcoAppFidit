from django.contrib import admin
from .models import *

# Register your models here.

model_list = [User, Organizer, EcoActivity, GroupAssistant]
admin.site.register(model_list)