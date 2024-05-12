from django.urls import path
from Quiz.views import home, quiz, cadastrar_quiz


urlpatterns = [
    path('', home),
    path('Quiz/', quiz),
    path('Cadastrar_Quiz/', cadastrar_quiz)
]
