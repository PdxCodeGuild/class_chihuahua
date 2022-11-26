from django.db import models
from datetime import date

class Todo(models.Model):
    description = models.CharField(max_length = 500)
    created_date = models.DateField()
    completed_todo = models.BooleanField()
    
    def __str__(self):
        return f'{self.description}, {self.created_date}, {self.completed_todo}'