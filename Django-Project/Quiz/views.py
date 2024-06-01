from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Option
from .forms import QuizForm, QuestionForm, OptionForm, UserForm


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
            quiz = form.save()
            quiz_uuid = quiz.uuid
            # Redireciona para a página inicial ou para onde for apropriado
            return redirect('add_quest', quiz_uuid=quiz_uuid)
    else:
        form = QuizForm()

    return render(request, 'Quiz/pages/create_quiz.html', {'form': form})


def add_quest(request, quiz_uuid):
    quiz_uuid = get_object_or_404(Quiz, uuid=quiz_uuid)

    if request.method == 'POST':
        form = QuestionForm(request.POST, initial={'quiz_uuid': quiz_uuid})
        if form.is_valid():
            question = form.save()
            question_uuid = question.uuid
            return redirect('add_option', question_uuid=question_uuid)
    else:
        form = QuestionForm(initial={'quiz_uuid': quiz_uuid})

    return render(request, 'Quiz/pages/add_quest.html', {'form': form})


def add_option(request, question_uuid):
    question_uuid = get_object_or_404(Question, uuid=question_uuid)

    if request.method == 'POST':
        form = OptionForm(request.POST, initial={
                          'question': question_uuid})
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OptionForm(initial={'question': question_uuid})

    return render(request, 'Quiz/pages/add_option.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()

    return render(request, 'Quiz/pages/create_user.html', {'form': form})
