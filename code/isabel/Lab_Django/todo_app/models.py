from django.db import models

# Create your models here.
class TodoItem:
    def __init__(self, text, start_date, end_date, completion_check):
        self.text = text
        self.start_date = start_date
        self.end_date = end_date
        self.completion_check = completion_check
        