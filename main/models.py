from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    # category choices
    JS = "Javascript"
    PY = 'Python'
    CSS = 'CSS'
    HTML = 'HTML'

    category_choices = [(JS, 'Javascript'), (PY, 'Python'), (CSS, 'CSS'), (HTML, 'HTML')]
    author = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    header_image = models.URLField(default='https://images.pexels.com/photos/270404/pexels-photo-270404.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    body = RichTextField()
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    category = models.CharField(choices=category_choices, max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title +' | '


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.body[0:10]
    