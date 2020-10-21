from django.http  import HttpResponse
from django.shortcuts import render
from .models import Question

def question_list(request):
    return HttpResponse('Home View')

def question_create(request, *args, **kwargs):
    return render(request, 'question/form.html', {})