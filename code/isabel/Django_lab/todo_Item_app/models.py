from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length = 200)
    task = models.CharField(max_length = 500)
    start_date = models.DateField()
    end_date = models.DateField()
    completion = models.BooleanField(default=False)

    def __str__(self):
        return self.title
