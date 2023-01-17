from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return self.task_name
