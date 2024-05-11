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

    def test_historic_deleted_events_multiple_events(self):
        # Create multiple historic deleted events
        events = [
            HistoricDeletedEvents.objects.create(
                name=f'Test Event {i}',
                executionDate=timezone.now(),
                place='Test Place',
                progress=0,
                user=self.user,
                deleted=timezone.now().date()
            ) for i in range(3)
        ]

        # Log in the user
        self.client.force_login(self.user)

        # Access the view for historic deleted events
        response = self.client.get(reverse('historic_deleted_events'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if all events are present in the context
        for event in events:
            self.assertIn(event, response.context['historic_events'])

    def test_historic_deleted_events_pagination(self):
        # Create more than the default number of historic deleted events
        for i in range(15):
            HistoricDeletedEvents.objects.create(
                name=f'Test Event {i}',
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

        # Check if only the default number of events are present in the context
        self.assertEqual(len(response.context['historic_events']), 10)

    def test_historic_deleted_events_superuser_access(self):
        # Create a superuser
        superuser = User.objects.create_superuser(username='superuser', password='12345')

        # Log in the superuser
        self.client.force_login(superuser)

        # Access the view for historic deleted events
        response = self.client.get(reverse('historic_deleted_events'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the view displays all historic deleted events for superuser
        self.assertEqual(response.context['historic_events'].count(), HistoricDeletedEvents.objects.count())

    def test_historic_deleted_events_non_superuser_access(self):
        # Create another user
        another_user = User.objects.create_user(username='anotheruser', password='12345')

        # Log in the another user
        self.client.force_login(another_user)

        # Access the view for historic deleted events
        response = self.client.get(reverse('historic_deleted_events'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the view displays only the historic deleted events of the logged-in user
        self.assertEqual(response.context['historic_events'].count(), HistoricDeletedEvents.objects.filter(user=another_user).count())

    def test_historic_deleted_events_pagination_page2(self):
        # Create more than the default number of historic deleted events
        for i in range(15):
            HistoricDeletedEvents.objects.create(
                name=f'Test Event {i}',
                executionDate=timezone.now(),
                place='Test Place',
                progress=0,
                user=self.user,
                deleted=timezone.now().date()
            )

        # Log in the user
        self.client.force_login(self.user)

        # Access the view for historic deleted events, page 2
        response = self.client.get(reverse('historic_deleted_events'), {'page': 2})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if only the remaining events are present in the context
        self.assertEqual(len(response.context['historic_events']), 5)

        def test_historic_deleted_events_pagination(self):
        # Create more than the default number of historic deleted events
         for i in range(15):
            HistoricDeletedEvents.objects.create(
                name=f'Test Event {i}',
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

        # Check if only the default number of events are present in the context
        self.assertEqual(len(response.context['historic_events']), 10)

    def test_historic_deleted_events_superuser_access(self):
        # Create a superuser
        superuser = User.objects.create_superuser(username='superuser', password='12345')

        # Log in the superuser
        self.client.force_login(superuser)

        # Access the view for historic deleted events
        response = self.client.get(reverse('historic_deleted_events'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the view displays all historic deleted events for superuser
        self.assertEqual(response.context['historic_events'].count(), HistoricDeletedEvents.objects.count())

    def test_historic_deleted_events_non_superuser_access(self):
        # Create another user
        another_user = User.objects.create_user(username='anotheruser', password='12345')

        # Log in the another user
        self.client.force_login(another_user)

        # Access the view for historic deleted events
        response = self.client.get(reverse('historic_deleted_events'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the view displays only the historic deleted events of the logged-in user
        self.assertEqual(response.context['historic_events'].count(), HistoricDeletedEvents.objects.filter(user=another_user).count())

    def test_historic_deleted_events_pagination_page2(self):
        # Create more than the default number of historic deleted events
        for i in range(15):
            HistoricDeletedEvents.objects.create(
                name=f'Test Event {i}',
                executionDate=timezone.now(),
                place='Test Place',
                progress=0,
                user=self.user,
                deleted=timezone.now().date()
            )

        # Log in the user
        self.client.force_login(self.user)

        # Access the view for historic deleted events, page 2
        response = self.client.get(reverse('historic_deleted_events'), {'page': 2})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if only the remaining events are present in the context
        self.assertEqual(len(response.context['historic_events']), 5)

