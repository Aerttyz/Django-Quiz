from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<uuid:id>/', views.quiz, name='quiz_detail'),
    path('Create_quiz/', views.create_quiz, name='create_quiz'),
    path('add_quest/<uuid:quiz_uuid>/', views.add_quest, name='add_quest'),
    path('add_option/<uuid:question_uuid>/',
         views.add_option, name='add_option'),
    path('create_user/', views.create_user, name='create_user'),
]
