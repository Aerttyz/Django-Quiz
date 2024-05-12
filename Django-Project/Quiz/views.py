from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'Quiz/pages/home.html')


def quiz(request):
    return HttpResponse('Uma feia string')


def cadastrar_quiz(request):
    return HttpResponse('Uma horrenda string')
