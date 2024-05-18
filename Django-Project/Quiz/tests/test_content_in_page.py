from .test_quiz_base import QuizBaseTest
from django.urls import reverse


class test_content_in_page(QuizBaseTest):

    def test_content_home_is_correct(self):
        user = self.make_user()  # Criar um usuário
        self.make_quiz(creator_uuid=user)  # Associar o usuário ao quiz
        response = self.client.get(reverse('home'))
        content = response.content.decode('utf-8')
        response_context_quiz = response.context['Quiz']
        self.assertIn('Quiz', content)
        self.assertIn('eb2fbd1c-1113-4931-894d-39db958833dc', content)
        self.assertIn('This is a sample quiz description.', content)
        self.assertEqual(len(response_context_quiz), 1)
        pass

    def test_content_Quiz_is_correct(self):
        user = self.make_user()
        quiz = self.make_quiz(creator_uuid=user)
        response = self.client.get(
            reverse('quiz_detail', args=[str(quiz.uuid)]))
        content = response.content.decode('utf-8')
        self.assertIn('Quiz', content)
        pass

    def test_content_create_quiz_is_correct(self):
        response = self.client.get(
            reverse('create_quiz'))
        content = response.content.decode('utf-8')
        self.assertIn('Quiz', content)
        pass

    def test_content_add_quest_is_correct(self):
        user = self.make_user()
        self.make_quiz(creator_uuid=user)
        response = self.client.get(
            reverse('add_quest'))
        content = response.content.decode('utf-8')
        self.assertIn('eb2fbd1c-1113-4931-894d-39db958833dc', content)
        pass

    def test_content_add_option_is_correct(self):
        user = self.make_user()
        self.make_quiz(creator_uuid=user)
        response = self.client.get(
            reverse('add_option'))
        content = response.content.decode('utf-8')
        self.assertIn('Quiz', content)
        pass

    def test_content_create_user_is_correct(self):
        response = self.client.get(
            reverse('create_user'))
        content = response.content.decode('utf-8')
        self.assertIn('Quiz', content)
        pass
