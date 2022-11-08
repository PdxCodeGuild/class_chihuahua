from django.db import models

# Create your models here.
class todo_item(models.Model):
    text = models.CharField(max_length = 200)
    date_started = models.DateField

    def __str__(self):
        return self.title