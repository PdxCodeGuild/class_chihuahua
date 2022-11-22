from django.db import models
from datetime import datetime
# Create your models here.
class todo_item(models.Model):
    title = models.TextField(max_length = 200, default = 'chore')
    text = models.TextField(max_length= 200)
    date_started = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title
