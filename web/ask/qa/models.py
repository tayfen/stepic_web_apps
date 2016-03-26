from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=20)
    likes = models.ManyToManyField(User, related_name='likes_set', null=True)

    def _get_url(self):
        return "http://127.0.0.1/question/%s" % (self.id)
        
    def __unicode__(self):              
        return self.title
    

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    #, default=1
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=20)
    
    def _get_url(self):
        return "http://127.0.0.1/question/%s" % (self.question.id)

    def __unicode__(self):              
        return self.text

