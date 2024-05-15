from django.shortcuts import render


def home(request):
    return render(request, 'Quiz/pages/home.html')


def quiz(request, id):
    return render(request, 'Quiz/pages/quiz.html')


def create_quiz(request):
    return render(request, 'Quiz/pages/create_quiz.html')


def login(request):
    return render(request, 'Quiz/pages/login.html')
