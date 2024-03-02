from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Organizer(models.Model):
    org_name = models.CharField(max_length=20)
    org_lastname = models.CharField(max_length=20)
    org_contact = models.EmailField()
    org_companyID = models.CharField(max_length=15)

    def __str__(self):
        return self.org_companyID

class EcoActivity(models.Model):
    eco_name = models.CharField(max_length=50)
    eco_summary = models.TextField()
    eco_date = models.DateTimeField(default=timezone.now)
    eco_author = models.ForeignKey(Organizer, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.eco_name

class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_lastname = models.CharField(max_length=20)
    user_id = models.CharField(max_length=15)
    user_activ = models.ManyToManyField(EcoActivity)

    def __str__(self):
        return self.user_id

class GroupAssistant(models.Model):
    mentor = models.OneToOneField(Organizer, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ass_task = models.CharField(max_length=30)
    ass_done = models.BooleanField(default=False)

    def __str__(self):
        return 'Asistentski podaci usera sa ID-em {}'.format(self.user.user_id)