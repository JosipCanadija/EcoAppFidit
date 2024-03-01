from django.contrib import admin
from .models import *

# Register your models here.

model_list = [UserProfile, UserEcoAction, EcoAction]
admin.site.register(model_list)