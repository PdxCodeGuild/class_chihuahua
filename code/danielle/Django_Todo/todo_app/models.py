from django.db import models
from datetime import date

class Todo(models.Model):
    description = models.CharField(max_length = 500)
    created_date = models.DateField()
    incomplete_todo = models.BooleanField(default=False)
    completed_todo = models.BooleanField(default=False)

    def __str__(self):
        return self.description