from django import forms
from django.forms import ModelForm
from .models import Question, Answer, User

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question

#class AskForm(ModelForm):
#    class Meta:
#        model = Question
#        fields = ['text', 'title']
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

#class AnswerForm(ModelForm):
#    class Meta:
#        model = Answer
#        fields = ['text', 'question']
#text = forms.CharField(widget=forms.Textarea)
#question = forms.CharField()


class AnswerForm(forms.Form):
    text = forms.CharField(max_length=100)
    question = forms.IntegerField()
    #hidden = forms.CharField(widget=forms.HiddenInput())

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
