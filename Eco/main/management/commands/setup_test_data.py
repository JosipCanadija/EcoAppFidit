from django.core.management.base import BaseCommand
from django.db import transaction
import random
from main.factory import OrganizerFactory, EcoActivityFactory, GroupAssistantFactory, UserFactory
from main.models import Organizer, EcoActivity, GroupAssistant, User

NUM_ORGANIZERS = 10
NUM_ECO_ACTIVITIES = 20
NUM_GROUP_ASSISTANTS = 30
NUM_USERS = 50


class Command(BaseCommand):
    help = "Generates test data for organizers, eco activities, group assistants, and users"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Organizer, EcoActivity, GroupAssistant, User]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_ORGANIZERS):
            organizer = OrganizerFactory()

        for _ in range(NUM_ECO_ACTIVITIES):
            eco_activity = EcoActivityFactory()

        for _ in range(NUM_GROUP_ASSISTANTS):
            group_assistant = GroupAssistantFactory()

        for _ in range(NUM_USERS):
            user = UserFactory()

        self.stdout.write(self.style.SUCCESS("Test data generated successfully!"))
