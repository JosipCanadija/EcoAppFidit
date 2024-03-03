from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.utils import timezone
from .models import *
from .views import *

class ModelsTestCase(TestCase):
    def setUp(self):
        self.organizer = Organizer.objects.create(org_name='John', org_lastname='Doe', org_contact='john@example.com', org_companyID='123')
        self.eco_activity = EcoActivity.objects.create(eco_name='Activity', eco_summary='Summary', eco_date=timezone.now(), eco_author=self.organizer)
        self.user = User.objects.create(user_name='Alice', user_lastname='Smith', user_id='user123')
        self.group_assistant = GroupAssistant.objects.create(mentor=self.organizer, user=self.user, ass_task='Task', ass_done=False)

    def test_organizer_creation(self):
        self.assertEqual(self.organizer.org_name, 'John')
        self.assertEqual(self.organizer.org_lastname, 'Doe')
        self.assertEqual(self.organizer.org_contact, 'john@example.com')
        self.assertEqual(self.organizer.org_companyID, '123')

    def test_eco_activity_creation(self):
        self.assertEqual(self.eco_activity.eco_name, 'Activity')
        self.assertEqual(self.eco_activity.eco_summary, 'Summary')
        self.assertTrue(isinstance(self.eco_activity.eco_date, timezone.datetime))
        self.assertEqual(self.eco_activity.eco_author, self.organizer)

    def test_user_creation(self):
        self.assertEqual(self.user.user_name, 'Alice')
        self.assertEqual(self.user.user_lastname, 'Smith')
        self.assertEqual(self.user.user_id, 'user123')

    def test_group_assistant_creation(self):
        self.assertEqual(self.group_assistant.mentor, self.organizer)
        self.assertEqual(self.group_assistant.user, self.user)
        self.assertEqual(self.group_assistant.ass_task, 'Task')
        self.assertFalse(self.group_assistant.ass_done)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('Eco:landing')
        self.organizers_url = reverse('Eco:listOrg')

        self.organizer = Organizer.objects.create(
            org_name='Test Org Name',
            org_lastname='Test Org Lastname',
            org_contact='test@example.com',
            org_companyID='test_company_id'
        )

    def test_base_generic_GET(self):
        response = self.client.get(self.homepage_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html')

    def test_organizers_list_GET(self):
        response = self.client.get(self.organizers_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_organizers.html')


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('Eco:landing')
        self.assertEquals(resolve(url).func.view_class, LandingPageView)

    def test_organizers_url_is_resolved(self):
        url = reverse('Eco:listOrg')
        self.assertEquals(resolve(url).func.view_class, OrganizerListView)

    def test_eco_activities_url_is_resolved(self):
        url = reverse('Eco:listEco')
        self.assertEquals(resolve(url).func.view_class, EcoActivityListView)

    def test_users_url_is_resolved(self):
        url = reverse('Eco:listUsers')
        self.assertEquals(resolve(url).func.view_class, UserListView)

    def test_group_assistants_url_is_resolved(self):
        url = reverse('Eco:listAssistants')
        self.assertEquals(resolve(url).func.view_class, GroupAssistantListView)

    def test_organizer_create_url_is_resolved(self):
        url = reverse('Eco:addOrganizers')
        self.assertEquals(resolve(url).func.view_class, OrganizerCreateView)

    def test_eco_activity_create_url_is_resolved(self):
        url = reverse('Eco:addEco')
        self.assertEquals(resolve(url).func.view_class, EcoActivityCreateView)

    def test_user_create_url_is_resolved(self):
        url = reverse('Eco:addUser')
        self.assertEquals(resolve(url).func.view_class, UserCreateView)

    def test_group_assistant_create_url_is_resolved(self):
        url = reverse('Eco:addAssistant')
        self.assertEquals(resolve(url).func.view_class, GroupAssistantCreateView)

    def test_group_assistant_update_url_is_resolved(self):
        url = reverse('Eco:updateAssistant', args=[1])
        self.assertEquals(resolve(url).func.view_class, GroupAssistantUpdateView)

    def test_group_assistant_delete_url_is_resolved(self):
        url = reverse('Eco:deleteAssistant', args=[1])
        self.assertEquals(resolve(url).func.view_class, GroupAssistantDeleteView)

    def test_user_update_url_is_resolved(self):
        url = reverse('Eco:updateUser', args=[1])
        self.assertEquals(resolve(url).func.view_class, UserUpdateView)

    def test_user_delete_url_is_resolved(self):
        url = reverse('Eco:deleteUser', args=[1])
        self.assertEquals(resolve(url).func.view_class, UserDeleteView)

    def test_eco_activity_update_url_is_resolved(self):
        url = reverse('Eco:updateEco', args=[1])
        self.assertEquals(resolve(url).func.view_class, EcoActivityUpdateView)

    def test_eco_activity_delete_url_is_resolved(self):
        url = reverse('Eco:deleteEco', args=[1])
        self.assertEquals(resolve(url).func.view_class, EcoActivityDeleteView)

    def test_organizer_update_url_is_resolved(self):
        url = reverse('Eco:updateOrganizers', args=[1])
        self.assertEquals(resolve(url).func.view_class, OrganizerUpdateView)

    def test_organizer_delete_url_is_resolved(self):
        url = reverse('Eco:deleteOrganizers', args=[1])
        self.assertEquals(resolve(url).func.view_class, OrganizerDeleteView)