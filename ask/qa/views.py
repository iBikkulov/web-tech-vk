from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

def test(request, question_id=None):
    return HttpResponse('OK')


@require_GET
def index(request):
    questions = Question.objects.new()
    paginator = Paginator(questions, 10)    # Show 10 questions per page
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'qa/index.html', {'questions': questions})


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'qa/question.html', {'question': question})