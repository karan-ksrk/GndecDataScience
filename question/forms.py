from django import forms
from .models import Question
# class QuestionForm(forms.Form):
  
#     question = forms.CharField(widget=forms.Textarea)
#     option1 = forms.CharField(widget=forms.Textarea)
#     option2 = forms.CharField(widget=forms.Textarea)
#     option3 = forms.CharField(widget=forms.Textarea)
#     option4 = forms.CharField(widget=forms.Textarea)
#     correct = forms.CharField()

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            "question",
            "option1",
            "option2",
            "option3",
            "option4",
            "correct",
            "tags",
        ]

    