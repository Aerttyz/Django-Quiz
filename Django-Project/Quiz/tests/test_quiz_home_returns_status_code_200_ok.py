from django.urls import reverse
from django.test import TestCase
from Quiz.models import Quiz
from User.models import User
from uuid import UUID


class Test_status_code(TestCase):
    def setUp(self):
        # Crie um objeto User no banco de dados de teste
        self.user = User.objects.create(
            # Ajuste conforme necessário
            uuid=UUID('12345678-1234-5678-1234-567812345678'),
            first_name='Test',
            last_name='User',
            email='test@example.com',
            password='testpassword',
            is_active=True,
            is_admin=False
        )

        # Crie um objeto Quiz associado ao usuário criado
        self.quiz = Quiz.objects.create(
            uuid=UUID('eb2fbd1c-1113-4931-894d-39db958833dc'),
            image='quiz/default.jpg',
            title='Sample Quiz',
            description='This is a sample quiz description.',
            creator_uuid=self.user,
            is_published=True
        )

    def test_content_is_correct(self):
        respose = self.client.get(reverse('home'))
        content = respose.content.decode('utf-8')
        self.assertIn('Quiz', content)
        pass

    def test_quiz_home_returns_status_code_200_ok(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_quiz_home_returns_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'Quiz/pages/home.html')

    def test_quiz_detail_returns_status_code_200_ok(self):
        response = self.client.get(
            reverse('quiz_detail', args=[
                    'eb2fbd1c-1113-4931-894d-39db958833dc'])
        )
        self.assertEqual(response.status_code, 200)

    def test_quiz_detail_loads_correct_template(self):
        example_uuid = 'eb2fbd1c-1113-4931-894d-39db958833dc'
        url = reverse('quiz_detail', args=[example_uuid])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'Quiz/pages/quiz.html')

    def test_create_quiz_returns_status_code_200_ok(self):
        response = self.client.get(reverse('create_quiz'))
        self.assertEqual(response.status_code, 200)

    def test_create_quiz_returns_loads_correct_template(self):
        response = self.client.get(reverse('create_quiz'))
        self.assertTemplateUsed(response, 'Quiz/pages/create_quiz.html')

    def test_add_quest_returns_status_code_200_ok(self):
        response = self.client.get(reverse('add_quest'))
        self.assertEqual(response.status_code, 200)

    def test_add_quest_returns_loads_correct_template(self):
        response = self.client.get(reverse('add_quest'))
        self.assertTemplateUsed(response, 'Quiz/pages/add_quest.html')

    def test_add_option_returns_status_code_200_ok(self):
        response = self.client.get(reverse('add_option'))
        self.assertEqual(response.status_code, 200)

    def test_add_option_returns_loads_correct_template(self):
        response = self.client.get(reverse('add_option'))
        self.assertTemplateUsed(response, 'Quiz/pages/add_option.html')

    def test_create_user_returns_status_code_200_ok(self):
        response = self.client.get(reverse('create_user'))
        self.assertEqual(response.status_code, 200)

    def test_create_user_returns_loads_correct_template(self):
        response = self.client.get(reverse('create_user'))
        self.assertTemplateUsed(response, 'Quiz/pages/create_user.html')
