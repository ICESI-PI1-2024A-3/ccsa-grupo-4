from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from logistic.models import HistoricDeletedEvents

class TestHistoricDeletedEvents(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()

    def test_historic_deleted_events(self):
        # Create a historic deleted event
        event = HistoricDeletedEvents.objects.create(
            name='Test Event',
            executionDate=timezone.now(),
            place='Test Place',
            progress=0,
            user=self.user,
            deleted=timezone.now().date()
        )

        # Log in the user
        self.client.force_login(self.user)

        # Access the view for historic deleted events
        response = self.client.get(reverse('historic_deleted_events'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the event is present in the context
        self.assertIn(event, response.context['historic_events'])

    def test_historic_deleted_events_no_login(self):
        # Access the view for historic deleted events without logging in
        response = self.client.get(reverse('historic_deleted_events'))

        # Check if the response status code is 302 (redirect to login)
        self.assertEqual(response.status_code, 302)

    def test_historic_deleted_events_no_events(self):
        # Log in the user
        self.client.force_login(self.user)

        # Access the view for historic deleted events
        response = self.client.get(reverse('historic_deleted_events'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if no historic events are present in the context
        self.assertQuerysetEqual(response.context['historic_events'], [])

    