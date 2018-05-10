from django.db import models


class Games(models.Model):
    hometeam = models.CharField(max_length=200)
    otherteam = models.CharField(max_length=200)
    homepoints = models.IntegerField(max_length=200)
    otherpoints = models.IntegerField(max_length=200)

