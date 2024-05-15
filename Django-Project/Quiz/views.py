from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Option


def home(request):
    quiz = Quiz.objects.all().order_by('-created_at')
    return render(request, 'Quiz/pages/home.html', context={'Quiz': quiz})


def quiz(request, id):
    quiz = get_object_or_404(Quiz, uuid=id, is_published=True)
    questions = quiz.question_set.all()
    return render(request, 'Quiz/pages/quiz.html', context={'quiz': quiz, 'questions': questions})


def create_quiz(request):
    return render(request, 'Quiz/pages/create_quiz.html')


def login(request):
    return render(request, 'Quiz/pages/login.html')
