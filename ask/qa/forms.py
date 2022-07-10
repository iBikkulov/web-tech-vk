from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

from .models import Question, Answer


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        # We need a Question object to create an Answer object
        question = Question.objects.get(pk=self.cleaned_data['question'])
        self.cleaned_data['question'] = question
        return Answer.objects.create(**self.cleaned_data)


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        return Question.objects.create(**self.cleaned_data)


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        widgets = {
            'email':    forms.EmailInput(),
            'password': forms.PasswordInput()
        }
        labels = {
            'username':     'Username',
            'email':        'Email',
            'password':     'Password',
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError('User "%s" already exists.' % username)
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        make_password(password, salt='some salt')
        return password
