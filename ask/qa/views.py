from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

def test(request, question_id=None):
    return HttpResponse('OK')

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'qa/question.html', {'question': question})