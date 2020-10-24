from django import forms

class QuestionForm(forms.Form):
  
    question = forms.CharField(widget=forms.Textarea)
    option1 = forms.CharField(widget=forms.Textarea)
    option2 = forms.CharField(widget=forms.Textarea)
    option3 = forms.CharField(widget=forms.Textarea)
    option4 = forms.CharField(widget=forms.Textarea)
    correct = forms.CharField()
