from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    thumbnail= models.CharField(max_length=500)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
