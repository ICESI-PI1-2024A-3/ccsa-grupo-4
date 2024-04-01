from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from ..models import Event
from ..models import Task

class TestTask(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.event = Event.objects.create(name='Test Event', executionDate=timezone.now() + timedelta(days=7), place='Test Place', progress=0, user=self.user)
        self.task = Task.objects.create(name='Test Task', event=self.event, user=self.user)

    def test_create_task_view(self):
        """ Test for: creating a task
        - The response for this would be first 200, which means that the form shows up 'OK'
        - Then, we test that the creation was succesfull, which means that the code should be 302 (was redirected to home) 
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse('create_task'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('create_task'), {'name': 'New Task', 'event': self.event.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='New Task').exists())