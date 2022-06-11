import datetime

from django.db import models
from django.utils import timezone

class Team(models.Model):
  syumoku = models.CharField(max_length=10)
  team_name = models.CharField(max_length=20)
  member1 = models.CharField(max_length=20, null=True)
  member2 = models.CharField(max_length=20, null=True)
  member3 = models.CharField(max_length=20, null=True)
  member4 = models.CharField(max_length=20, null=True)
  member5 = models.CharField(max_length=20, null=True)
  member6 = models.CharField(max_length=20, null=True)
  member7 = models.CharField(max_length=20, null=True)
  member8 = models.CharField(max_length=20, null=True)
  member9 = models.CharField(max_length=20, null=True)
  member10 = models.CharField(max_length=20, null=True)

class Order(models.Model):
  syumoku = models.CharField(max_length=10)
  team_name = models.CharField(max_length=20)
  enemy_name = models.CharField(max_length=20)
  single_6 = models.CharField(max_length=20)
  double_6_1 = models.CharField(max_length=20)
  double_6_2 = models.CharField(max_length=20)
  double_5 = models.CharField(max_length=20)
  double_5_1 = models.CharField(max_length=20)
  double_5_2 = models.CharField(max_length=20)
  double_4 = models.CharField(max_length=20)
