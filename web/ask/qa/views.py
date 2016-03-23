from django.shortcuts import render
from .models import Answer, Question
from django.core.paginator import Paginator

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, Http404
def test(request, question=0):
    if question != 0:
        return HttpResponse('OK')
    else:
        return HttpResponse('HTTP 404 test')

def top(request):
    posts = Question.objects.all().order_by('-added_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    return render (request, 'qa/new_q.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
    })
    
def pop(request):
    posts = Question.objects.all().order_by('-rating')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    paginator.baseurl = 'popular/?page='
    page = paginator.page(page)
    return render (request, 'qa/new_q.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def question(request, quest=0):
    try:
        q = Question.objects.get(id=quest)
        #answers = q.Answer.objects.get(question_id=quest)
        answers = Answer.objects.all().filter(question_id=quest)
        #answers = Answer.objects.select_related(q)
        return render(request, 'qa/question.html', {
        'question' : q,
        'answers' : answers,
        })
    except Question.DoesNotExist:
        raise Http404('no such question')
    return HttpResponse('HTTP 404 quest')

