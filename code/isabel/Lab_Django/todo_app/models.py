from django.db import models

# Create your models here.
# class TodoItem:
#     def __init__(self, text, start_date, end_date, completion_check):
#         self.text = text
#         self.start_date = start_date
#         self.end_date = end_date
#         self.completion_check = completion_check
class TodoItem(models.Model):
    text = models.CharField(max_length = 300)
    start_date = models.DateField()
    end_date = models.DateField()
    completion_check = models.BooleanField()

