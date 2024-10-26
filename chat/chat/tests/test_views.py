from django.test import TestCase
from django.urls import reverse

class HomeViewTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))  # Use the URL name of your home view
        self.assertEqual(response.status_code, 200)

    def test_home_view_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')