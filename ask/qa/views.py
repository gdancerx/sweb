from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from qa.models import Question, User
from qa.forms import AskForm, AnswerForm, SignupForm
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login

def get_page(request):
    page = request.GET.get('page')
    #questions = Question.objects.all().order_by('-added_at')
    questions = Question.objects.new()
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    try:
        q_to_show = paginator.page(page)
    except PageNotAnInteger:
        q_to_show = paginator.page(1)
    return render(request, 'page.html', {
        'questions': q_to_show.object_list,
        'paginator': paginator,
        'page': page,
    })

def get_popular(request):
    page = request.GET.get('page')
    questions = Question.objects.popular()
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    try:
        q_to_show = paginator.page(page)
    except PageNotAnInteger:
        q_to_show = paginator.page(1)
    return render(request, 'page.html', {
        'questions': q_to_show.object_list,
        'paginator': paginator,
        'page': page,
    })

def get_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            answer = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question.id})
    return render(request, 'question.html', {
        'q': question,
        'form': form,
    })

def add_question(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form
    })



