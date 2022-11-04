from django.db import models

class Todo(models.Model):
    description = models.TextField(max_length = 500)
    created_date = models.DateField()
    completed_date = models.DateField()
    #if completed_date == True:
            #print("item completed.")

    def __str__(self):
        return self.title
