from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<uuid:id>/', views.quiz, name='quiz_detail'),
    path('Create_quiz/', views.create_quiz, name='create_quiz'),
    path('Login/', views.login, name='login'),
]
