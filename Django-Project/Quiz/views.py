from django.shortcuts import render
from .models import Quiz, Question, Option


def home(request):
    quiz = Quiz.objects.all().order_by('-created_at')
    return render(request, 'Quiz/pages/home.html', context={'Quiz': quiz})


def quiz(request, id):
    question = Question.objects.get(quiz_uuid=id)
    return render(request, 'Quiz/pages/quiz.html', context={'Question': question})


def create_quiz(request):
    return render(request, 'Quiz/pages/create_quiz.html')


def login(request):
    return render(request, 'Quiz/pages/login.html')
