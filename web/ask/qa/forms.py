from django import forms
from django.forms import ModelForm
from .models import Question, Answer, User

class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'title']
        #def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
        #    question = super(AskForm, self).save(commit=False, *args, **kwargs)
        #    question = Question.objects.create()                            
        #    cd = self.cleaned_data
        #    author = User.objects.get(id=1)
        #    #question.title = cd['title']                                   
        #    #question.text = cd['text']                                     
        #    question.author = author
            #question.author_id = 1
         #   if commit:
         #       question.save()
         #   return question
#text = forms.CharField(widget=forms.Textarea)
#title = forms.CharField(widget=forms.Textarea, max_length=100)

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']
#text = forms.CharField(widget=forms.Textarea)
#question = forms.CharField()