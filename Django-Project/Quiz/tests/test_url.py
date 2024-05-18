from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Quiz import views


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    def test_quiz_detail_url(self):
        # Exemplo de UUID
        example_uuid = '123e4567-e89b-12d3-a456-426614174000'
        url = reverse('quiz_detail', args=[example_uuid])
        self.assertEqual(resolve(url).func, views.quiz)

    def test_create_quiz_url(self):
        url = reverse('create_quiz')
        self.assertEqual(resolve(url).func, views.create_quiz)

    def test_add_quest_url(self):
        url = reverse('add_quest')
        self.assertEqual(resolve(url).func, views.add_quest)

    def test_add_option_url(self):
        url = reverse('add_option')
        self.assertEqual(resolve(url).func, views.add_option)

    def test_create_user_url(self):
        url = reverse('create_user')
        self.assertEqual(resolve(url).func, views.create_user)
