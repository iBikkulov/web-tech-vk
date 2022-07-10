from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

from .models import Question, Answer


def make_password_custom(password):
    """Customized make_password function."""
    return make_password(password, salt='some salt')


class AnswerForm(forms.Form):
    """From for adding a new answer."""
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        try:
            author = User.objects.get(username=self._user.username)
        except User.DoesNotExist:
            raise ValidationError('User not exist or unauthorized.')
        self.cleaned_data['author'] = author

    def save(self):
        # We need a Question object to create an Answer object
        question = Question.objects.get(pk=self.cleaned_data['question'])
        self.cleaned_data['question'] = question
        return Answer.objects.create(**self.cleaned_data)


class AskForm(forms.Form):
    """Form for adding a new question."""
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        try:
            author = User.objects.get(username=self._user.username)
        except User.DoesNotExist:
            raise ValidationError('User "%s" does not exist.' % _user.username)
        self.cleaned_data['author'] = author

    def save(self):
        return Question.objects.create(**self.cleaned_data)


class SignupForm(forms.ModelForm):
    """Website signup form."""
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'email':    forms.EmailInput(),
            'password': forms.PasswordInput()
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError('User "%s" already exists.' % username)
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        return make_password_custom(password)


class SigninForm(forms.ModelForm):
    """Website signup form."""
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        # Note: doesn't work when the superuser logs in, because
        # a different salt was used when creating his password.
        password = make_password_custom(password)
        try:
            # Note: with current MySQL settings collations are case insensitive,
            # so for example 'asd' and 'Asd' are considered the same.
            self.instance = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            raise ValidationError('Username or password is incorrect!')
        return self.cleaned_data