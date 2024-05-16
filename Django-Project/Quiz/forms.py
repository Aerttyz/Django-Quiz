from django import forms
from .models import Quiz, Question, Option
from User.models import User


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
    required_css_class = 'required-field'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if field.required:
                field.widget.attrs['class'] = field.widget.attrs.get(
                    'class', '') + ' ' + self.required_css_class


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'quiz_uuid']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
            'quiz_uuid': forms.Select(attrs={'class': 'form-control'}),
        }
    required_css_class = 'required-field'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if field.required:
                field.widget.attrs['class'] = field.widget.attrs.get(
                    'class', '') + ' ' + self.required_css_class


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option_text', 'is_correct', 'question']
        widgets = {
            'option_text': forms.TextInput(attrs={'class': 'form-control'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # noqa: E501
            'question': forms.Select(attrs={'class': 'form-control'}),
        }
    required_css_class = 'required-field'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if field.required:
                field.widget.attrs['class'] = field.widget.attrs.get(
                    'class', '') + ' ' + self.required_css_class


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'fisrt_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # noqa: E501
        }
    required_css_class = 'required-field'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if field.required:
                field.widget.attrs['class'] = field.widget.attrs.get(
                    'class', '') + ' ' + self.required_css_class
