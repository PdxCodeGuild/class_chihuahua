from django.db import models

class Todo(models.Model):
    description = models.CharField(max_length = 500)
    created_date = models.DateField()
    completed_date = models.DateField()
    
    def __str__(self):
        return f'{self.description}, {self.created_date}, {self.completed_date}'