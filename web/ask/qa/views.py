from django.shortcuts import render
from .models import Answer, Question, User
from django.core.paginator import Paginator
from .forms import AnswerForm, AskForm

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
def test(request, question=0):
    if question != 0:
        return HttpResponse('OK')
    else:
        return HttpResponse('HTTP 404 test')

def top(request):
    posts = Question.objects.all().order_by('-id')
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

@csrf_protect
def question(request, quest=0):
    try:
        form = AnswerForm()
        q = Question.objects.get(id=quest)
        answers = q.answer_set.all()
        #answers = Answer.objects.all().filter(question_id=quest)
        #answers = Answer.objects.select_related(q)
        return render(request, 'qa/question.html', {
        'question' : q,
        'answers' : answers,
        'form' : form,
        })
    except Question.DoesNotExist:
        raise Http404('no such question')
    return HttpResponse('HTTP 404 quest')

@csrf_protect
def ask(request):
    if request.method == "GET":
    #if request.method == "POST":
        form = AskForm()
        return render(request, 'qa/ask.html', {
        'form' : form,
        })
    else:
        form = AskForm(request.POST)
        #author = User(id=1)
        #form = AskForm(request.GET)
        if form.is_valid():
            post = form.save()
            url = post._get_url()
            #return HttpResponse('dsa')
            return HttpResponseRedirect(url)
            #return HttpResponseRedirect("http://127.0.0.1")
        else:
            return HttpResponseRedirect("http://127.0.0.1/question/1/")
            #raise Http404('bad form')

@csrf_protect
def answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        post = form.save()
        url = post._get_url()
        return HttpResponseRedirect(url)
    else:
        raise Http404('bad form')
