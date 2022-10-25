from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.title