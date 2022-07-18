from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Question
from .forms import AnswerForm, AskForm, SignupForm, SigninForm


def index(request):
    questions = Question.objects.new()
    paginator = Paginator(questions, 3)    # Show 3 questions per page
    page_num = request.GET.get('page')
    questions = paginator.get_page(page_num)
    return render(request, 'qa/index.html', {'questions': questions})


def popular(request):
    questions = Question.objects.popular()
    paginator = Paginator(questions, 3)    # Show 3 questions per page
    page_num = request.GET.get('page')
    questions = paginator.get_page(page_num)
    return render(request, 'qa/popular.html', {'questions': questions})


def question(request, question_id):
    """
    Responsible for showing the page with answers to a question
    and processing the form for adding answers.
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, question_id=question.id)
        form._user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('question', args=(question.id,)))
    else:
        form = AnswerForm(question_id=question.id)
    return render(request, 'qa/question.html', {
        'question': question,
        'form': form
    })


@login_required(login_url='/login/')
def ask(request):
    """Responsible for processing the form for adding questions."""
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(reverse('question', args=(question.id,)))
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def signup(request):
    logout(request)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password']
            )
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SigninForm()
    return render(request, 'qa/signin.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))