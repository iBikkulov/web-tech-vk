from django.shortcuts import render
from django.http import HttpResponse

def test(request, question_id=None):
    return HttpResponse('OK')