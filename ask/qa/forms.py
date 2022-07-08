from django import forms
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