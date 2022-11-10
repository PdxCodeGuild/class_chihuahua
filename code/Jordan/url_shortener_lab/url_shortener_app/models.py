from django.db import models

class Url(models.Model):
    url_input = models.CharField(max_length=9999)
    url_output = models.CharField(max_length=13)
