from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from .forms import AnswerForm


def test(request, question_id=None):
    return HttpResponse('OK')


def index(request):
    questions = Question.objects.new()
    paginator = Paginator(questions, 10)    # Show 10 questions per page
    page_num = request.GET.get('page')
    questions = paginator.get_page(page_num)
    return render(request, 'qa/index.html', {'questions': questions})


def popular(request):
    questions = Question.objects.popular()
    paginator = Paginator(questions, 10)    # Show 10 questions per page
    page_num = request.GET.get('page')
    questions = paginator.get_page(page_num)
    return render(request, 'qa/popular.html', {'questions': questions})


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, initial={'question': question.id})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('question', args=(question.id,)))
    else:
        form = AnswerForm(initial={'question': question.id})
    return render(request, 'qa/question.html', {
        'question': question,
        'form': form
    })