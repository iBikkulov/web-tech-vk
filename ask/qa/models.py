from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new():
        return self.order_by('-added_at')
    
    def popular():
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Use 'related name' to prevent an error due to creating managers with same name
    likes = models.ManyToManyField(User, related_name='likes_set')

    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)