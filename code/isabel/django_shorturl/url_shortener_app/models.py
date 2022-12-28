from django.db import models

# Create your models here.
class Short(models.Model):
        code = models.CharField(max_length=800)
        url = models.CharField(max_length=800)

        # def __str__(self):
        #     return self.title
