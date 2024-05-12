from django.db import models
from User.models import User


class Quiz(models.Model):
    uuid = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_published = models.BooleanField(default=False)

    creator_uuid = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='uuid')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Question(models.Model):
    uuid = models.UUIDField(primary_key=True)
    question_text = models.CharField(max_length=255)

    quiz_uuid = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, to_field='uuid')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Option(models.Model):
    uuid = models.UUIDField(primary_key=True)
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, to_field='uuid')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
