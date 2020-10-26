from django.contrib.auth.decorators import  login_required
from django.contrib import messages
from django.http  import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question
from .forms import QuestionForm
from taggit.models import Tag

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
    common_tags = Question.tags.most_common()[:4]
    failed = False
    if request.method == "POST":
        post_data = request.POST or None
        if post_data != None:
            form = QuestionForm(request.POST)
            print(form)
            if form.is_valid():
                newques = form.save(commit=False)
                newques.user = request.user
                newques.save()
                form.save_m2m()
                messages.success(request, 'Success!')
            else:
                print("ERROR :", form.errors)
                failed = True
    ques_obj = Question.objects.all().filter(user=request.user)
    context = {
        'questions': ques_obj,
        'user': str(request.user).upper(),
        'form': QuestionForm(),
        'common_tags': common_tags,
        'failed': failed,
    }
    return render(request, 'question/form.html', context)


def tagged(request, id):
    tag = get_object_or_404(Tag, id=id)
    questions = Question.objects.filter(user=request.user).filter(tags=tag)
    context = {
        'tag': tag,
        'ques': questions,
    }
    return render(request, 'question/home.html', context)