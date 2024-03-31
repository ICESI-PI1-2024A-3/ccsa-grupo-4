from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from logistic.models import Event
from logistic.models import Task
from logistic.forms.eventForm import EventForm
from logistic.forms.taskForm import TaskChecklist
from django.contrib.auth.models import User
from datetime import timedelta

class test_Event(TestCase):
    #Creamos un usuario y evento para probar los métodos
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.event = Event.objects.create(name='Test Event', executionDate=timezone.now() + timedelta(days=7), place='Test Place', progress=0, user=self.user)


    def test_create_event(self):
        """ Test for: creating a new event in the database.
        
        - First, we authenticate the user with force_login.
        - Then, we capture the response of the page when creating the event.
        - Finally, after creating the event, the status code of the page would be 200, which is 'OK' and means that the request was successful.
        """
        self.client.force_login(self.user)
        response = self.client.post(reverse('create_event'), {'name': 'New Event', 'executionDate': timezone.now() + timedelta(days=7), 'place': 'New Place', 'progress': 0})
        self.assertEqual(response.status_code, 200)


    def test_create_event2(self):
        """ Test for: Creating a new event with a not valid input

        - The response of this would be 200, since the request was succesfull
          and it doesn't show up any unexpected error, just the normal ValueError that is controled
        """
        self.client.force_login(self.user)
        response = self.client.post(reverse('create_event'), {'name': 'New Event2', 'executionDate': "valorNoValido", 'place': 'Hall de auditorios', "progress": 20 })
        self.assertEqual(response.status_code, 200)

    def test_edit_event(self):
        """ Test for: edit an event already created
        - The response of this would be 200, since the edit was made succesfully
        """
        self.client.force_login(self.user)
        response = self.client.post(reverse('edit_event', args=[self.event.id]), {'name': 'Updated Event', 'executionDate': timezone.now() + timedelta(days=14), 'place': 'Updated Place', 'progress': 50})
        self.assertEqual(response.status_code, 200)

    def test_edit_event2(self):
        """Test for: edit an event that doesn't exit
        - We use and Id that does not correspond to any event.
        - The response of this would be 404, page not found, because the event does not exit
        """
        self.client.force_login(self.user)
        event_id_non_exist = 123
        response = self.client.post(reverse('edit_event', args=[event_id_non_exist]), {'name': 'Updated Event That Not Exist', 'executionDate': timezone.now() + timedelta(days=7), 'place': 'Updated Place 2', 'progress': 80 })
        self.assertEqual(response.status_code, 404)

    def test_complete_event(self):
        """Test for: mark an event as completed
        - The response of this would be 302, which means is redirected to another page temporally
        """
        self.client.force_login(self.user)
        response = self.client.post(reverse('event_complete', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)

    def test_complete_event2(self):
        """Test for: mark an event that doesn't exist as completed
        - The response of this would be 404, which means that the event wasn't found
        """
        self.client.force_login(self.user)
        event_id_non_exist = 123
        response = self.client.post(reverse('event_complete', args=[event_id_non_exist]))
        self.assertEqual(response.status_code, 404)

    def test_delete_event(self):
        """Test for: delete an event
        - The response of this would be 302, which means is redirected to home
        """
        self.client.force_login(self.user)
        response = self.client.post(reverse('event_delete', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_event2(self):
        """Test for: delete an event that doesn't exist
        - The response of this would be 404, which means that the event wasn't found
        """
        event_id_non_exist = 123
        self.client.force_login(self.user)
        response = self.client.post(reverse('event_delete', args=[event_id_non_exist]))
        self.assertEqual(response.status_code, 404)
        