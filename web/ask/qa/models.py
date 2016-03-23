from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=120)
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	likes = models.ManyToManyField(User, related_name='likes_set')
    
    def get_url(self):
        return "question/"+self.id

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	
