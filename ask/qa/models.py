from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=150)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name = 'likes_set')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.OneToOneField(Question)
    author = models.ForeignKey(User)

class QuestionManager(models.Manager):
    def new():
        pass
    def popular():
        pass
   
