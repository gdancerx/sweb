from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        return Question.objects.order_by('-added_at')
    def popular(self):
        return Question.objects.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=150)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1)
    likes = models.ManyToManyField(User, related_name = 'likes_set')
    def __unicode__(self):
        return self.title
    def get_url(self):
        return reverse('get_question', kwargs = {'question_id': self.id})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, default=1)
    def __unicode__(self):
        return self.text
