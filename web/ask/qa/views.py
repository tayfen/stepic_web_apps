from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound
def test(request, question=0):
    if question != 0:
        return HttpResponse('OK')
    else:
        return HttpResponse('HTTP 404')

def top(request):
    return HttpResponse('OK')
    
def pop(request):
    return HttpResponse('OK')
    
def question(request, question=0):
    try:
        quest = Question.objects.get(id=question)
    except Question.DoesNotExist:
		raise Http404
	return HttpResponse('HTTP 404')

