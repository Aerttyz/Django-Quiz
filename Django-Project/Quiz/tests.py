from django.test import TestCase
from django.urls import reverse


class QuizUrlTest(TestCase):
    def test_quiz_home_url_is_correct(self):
        url = reverse('home')
        self.assertEqual(url, '/')
