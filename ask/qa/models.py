from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    
    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Use 'related name' to prevent an error due to creating managers with same name
    likes = models.ManyToManyField(User, related_name='likes_set', default=None, blank=True)
    rating = models.IntegerField(default=0)

    objects = QuestionManager()

    def rate(self, user):
        if self.likes.filter(id=user.id).exists():
            self.likes.remove(user)
            self.rating -= 1
        else:
            self.likes.add(user)
            self.rating += 1
        self.save()
        return self.rating


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)