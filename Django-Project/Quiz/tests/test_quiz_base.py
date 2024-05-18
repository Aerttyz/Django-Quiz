from django.test import TestCase
from Quiz.models import Quiz
from User.models import User
from uuid import UUID


class QuizBaseTest(TestCase):

    def make_user(
        self,
        uuid=UUID('12345678-1234-5678-1234-567812345678'),
        first_name='Test',
        last_name='User',
        email='test@example.com',
        password='testpassword',
        is_active=True,
        is_admin=False
    ):
        return User.objects.create(
            uuid=uuid,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_active=is_active,
            is_admin=is_admin
        )

    def make_quiz(
        self,
        uuid=UUID('eb2fbd1c-1113-4931-894d-39db958833dc'),
        image='quiz/default.jpg',
        title='Sample Quiz',
        description='This is a sample quiz description.',
        creator_uuid=None,
        is_published=True
    ):
        if creator_uuid is None:
            creator_uuid = self.user
        return Quiz.objects.create(
            uuid=uuid,
            image=image,
            title=title,
            description=description,
            creator_uuid=creator_uuid,
            is_published=is_published
        )
