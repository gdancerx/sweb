from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponse
from qa.models import Question, User

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
    return render(request, 'question.html', {
        'question': question,
    })


