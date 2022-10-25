from django.db import models

class Drink(models.Model):
    drink_name = models.CharField(max_length=50, unique=True )
    drink_url = models.CharField(max_length=100, unique=True )
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.drink_name