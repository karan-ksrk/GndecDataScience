from django.http  import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Question
from .forms import QuestionForm


def question_list(request):
    return HttpResponse('Home View')

def question_create(request, *args, **kwargs):
  
    if request.method == "POST":
        post_data = request.POST or None
        if post_data != None:
            print(request.POST)
            form = QuestionForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                ques_object = Question.objects.create(**data)
                form = QuestionForm()
                ques_object.save()
    return render(request, 'question/form.html', {})