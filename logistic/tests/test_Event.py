from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from logistic.models import Event
from logistic.models import Task
from logistic.forms.eventForm import EventForm
from logistic.forms.taskForm import TaskChecklist
from django.contrib.auth.models import User
from datetime import datetime
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