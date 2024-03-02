##factory.py
import factory
import random
from factory.django import DjangoModelFactory
from main.models import *
from django.utils import timezone

class OrganizerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organizer

    org_name = factory.Faker('first_name')
    org_lastname = factory.Faker('last_name')
    org_contact = factory.Faker('email')
    org_companyID = factory.Sequence(lambda n: f'companyID-{n}')

class EcoActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EcoActivity

    eco_name = factory.Faker('sentence', nb_words=4)
    eco_summary = factory.Faker('text')
    eco_date = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    eco_author = factory.SubFactory(OrganizerFactory)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    user_name = factory.Faker('first_name')
    user_lastname = factory.Faker('last_name')
    user_id = factory.Sequence(lambda n: f'user_id_{n}')

    @factory.post_generation
    def user_activ(self, create, extracted, **kwargs):
        if extracted:
            for activity in extracted:
                self.user_activ.add(activity)
        else:
            num_activities = random.randint(1, 4)
            activities = EcoActivity.objects.order_by('?')[:num_activities]
            for activity in activities:
                self.user_activ.add(activity)

class GroupAssistantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupAssistant

    mentor = factory.SubFactory(OrganizerFactory)
    user = factory.SubFactory(UserFactory)
    ass_task = factory.Faker('sentence', nb_words=3)
    ass_done = False  