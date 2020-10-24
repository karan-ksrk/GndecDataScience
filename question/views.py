from django.contrib.auth.decorators import  login_required
from django.http  import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Question
from .forms import QuestionForm

@login_required
def question_list(request, *args, **kwargs):
    ques_obj = Question.objects.all().filter(user=request.user)
    context = {
        'questions': ques_obj,
        'user': str(request.user).upper(),
    }
    return render(request, 'question/home.html', context)

@login_required
def question_create(request, *args, **kwargs):
  
    if request.method == "POST":
        post_data = request.POST or None
        if post_data != None:
            form = QuestionForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                ques_object = Question.objects.create(**data)
                ques_object.user = request.user
                form = QuestionForm()
                ques_object.save()
    return render(request, 'question/form.html', {})