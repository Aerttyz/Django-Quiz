from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('Quiz/<uuid:id>/', views.quiz),
    path('Create_quiz/', views.create_quiz)
]
