from django.db import models

class Blog(models.Model):
        title = models.CharField(max_length = 200)
        text = models.TextField(max_length = 500)
        updated_date = models.DateTimeField(auto_now=True) #auto_now unpdating to the database
        created_date = models.DateTimeField(auto_now_add=True) #adding is whenever I'm creating
        completed_date = models.DateTimeField(auto_now_add=True) #need to create a view
        completed_task = models.BooleanField(default=False) #default to false because True means it is completed, while false means it hasn't

        def __str__(self):
            return self.title