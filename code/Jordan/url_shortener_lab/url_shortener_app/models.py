from django.db import models

class Url(models.Model):
    long_url = models.CharField(max_length=9999)
    short_url = models.CharField(max_length=13)
