from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Option
from .forms import QuizForm, QuestionForm, OptionForm


def home(request):
    quizs = Quiz.objects.all().order_by('-created_at')
    for quiz in quizs:
        author = quiz.creator_uuid.last_name + ', ' + quiz.creator_uuid.first_name  # noqa: E501
        quiz.author = author
    return render(request, 'Quiz/pages/home.html', context={'Quiz': quizs})  # noqa: E501


def quiz(request, id):
    quiz = get_object_or_404(Quiz, uuid=id, is_published=True)
    questions = quiz.question_set.all()
    for question in questions:
        option = question.option_set.all()
        question.options = option
    return render(request, 'Quiz/pages/quiz.html', context={'quiz': quiz, 'questions': questions})  # noqa: E501


def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redireciona para a página inicial ou para onde for apropriado
            return redirect('add_quest')
    else:
        form = QuizForm()

    return render(request, 'Quiz/pages/create_quiz.html', {'form': form})


def add_quest(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_option')
    else:
        form = QuestionForm()

    return render(request, 'Quiz/pages/add_quest.html', {'form': form})


def add_option(request):
    if request.method == 'POST':
        form = OptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OptionForm()

    return render(request, 'Quiz/pages/add_option.html', {'form': form})
