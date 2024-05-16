from django import forms
from .models import Quiz, Question, Option


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'image', 'description',
                  'is_published', 'creator_uuid']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # noqa: E501
            'creator_uuid': forms.Select(attrs={'class': 'form-control'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'quiz_uuid']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
            'quiz_uuid': forms.Select(attrs={'class': 'form-control'}),
        }


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option_text', 'is_correct', 'question']
        widgets = {
            'option_text': forms.TextInput(attrs={'class': 'form-control'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # noqa: E501
            'question': forms.Select(attrs={'class': 'form-control'}),
        }
