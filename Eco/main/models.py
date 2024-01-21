from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=300, blank=True)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username

class EcoAction(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    points = models.BooleanField()

    def __str__(self):
        return self.name

class UserEcoAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eco_action = models.ForeignKey(EcoAction, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.eco_action.name}"
