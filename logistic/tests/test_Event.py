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

    #Probamos que se puede crear un nuevo evento
    def test_create_event(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('create_event'), {'name': 'New Event', 'executionDate': timezone.now() + timedelta(days=7), 'place': 'New Place', 'progress': 0})
        self.assertEqual(response.status_code, 200)  # el código 200 significa 'OK' y que se agregó 
