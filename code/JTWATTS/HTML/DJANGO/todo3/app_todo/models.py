from django.db import models
from datetime import datetime


class Todo(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField(max_length = 500)
    status = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    completion = models.DateTimeField(blank=True, null=True) 
    TODO_TYPE = (
        ('p', 'personal'),
        ('s', 'school'),
        ('w', 'work'),
        ('f', 'family'),
        ('m', 'misc'),
    )

    todo_type = models.CharField(max_length = 1, choices = TODO_TYPE, blank = True, default = 'm')

    def __str__(self):
        return self.title

# Create your models here.
