from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound
def test(request, question=0):
    if question != 0:
        return HttpResponse('OK')
    else:
        return HttpResponse('HTTP 404')


