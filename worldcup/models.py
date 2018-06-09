from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Group(models.Model):
    character = models.CharField(max_length=1)


class Team(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    games_played = models.IntegerField()
    points = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    loses = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    goals_diff = models.IntegerField()


class Game(models.Model):
    home = models.ForeignKey(Team, related_name="home",
                             on_delete=models.CASCADE)
    away = models.ForeignKey(Team, related_name="away",
                             on_delete=models.CASCADE)
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()


class Profile(models.Model):
    name = models.CharField(max_length=200, default="name")
    top_scorer = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
