from django.contrib import admin
from .models import Quiz, Question, Option
from User.models import User


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)
