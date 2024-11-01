from django.test import TestCase
from django.urls import reverse
import unittest
from unittest.mock import patch, MagicMock
from views.py import question

class HomeViewTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))  # Use the URL name of your home view
        self.assertEqual(response.status_code, 200)

    def test_home_view_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    class TestQuestionFunction(unittest.TestCase):
    @patch('your_module.genai.GenerativeModel')
    def test_question(self, MockGenerativeModel):
        prompt = "Hello, AI!"
        expected_message = "Hello, how can I assist you?"
        
        mock_model = MockGenerativeModel.return_value
        mock_response = MagicMock()
        mock_response.text = expected_message
        mock_model.generate_content.return_value = mock_response

        result = question(prompt)

        self.assertEqual(result, expected_message)
        MockGenerativeModel.assert_called_once_with("gemini-1.5-flash")
        mock_model.generate_content.assert_called_once_with(prompt)