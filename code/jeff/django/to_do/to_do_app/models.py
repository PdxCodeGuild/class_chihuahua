from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    created_date = models.DateTimeField()
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title



