from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Event
from django.utils import timezone

class EventCalendarTest(TestCase):
    """
    Test suite for the calendar functionality in the Django application.
    """

    def setUp(self):
        """
        Sets up the test environment before each test method is executed.
        Creates a user, logs in the user, and creates an event associated with the user.
        """
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        
        # Create an event
        self.event = Event.objects.create(
            name="Test Event",
            executionDate=timezone.now(),
            place="Test Location",
            progress=50,
            finishDate=timezone.now() + timezone.timedelta(days=1),
            important=True,
            user=self.user
        )

    def test_calendar_access_for_superuser(self):
        """
        Tests that a superuser can access the calendar page.
        """
        # Create and log in as a superuser
        User.objects.create_superuser('admin', 'admin@admin.com', 'adminpass')
        self.client.login(username='admin', password='adminpass')
        
        response = self.client.get(reverse('events_calendar'))
        self.assertEqual(response.status_code, 200)

    def test_calendar_access_for_regular_user(self):
        """
        Tests that a regular user can access the calendar page.
        """
        response = self.client.get(reverse('events_calendar'))
        self.assertEqual(response.status_code, 200)



      


