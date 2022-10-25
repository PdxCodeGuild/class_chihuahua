from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    team_name = models.ManyToManyField(Team)


    def __str__(self):
        return self.first_name
