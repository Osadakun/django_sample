import datetime

from django.db import models
from django.utils import timezone

class Team(models.Model):
  team_name = models.CharField(max_length=20)
  member1 = models.CharField(max_length=20)
  member2 = models.CharField(max_length=20)
  member3 = models.CharField(max_length=20)
  member4 = models.CharField(max_length=20)
  member5 = models.CharField(max_length=20)
  member6 = models.CharField(max_length=20)
  member7 = models.CharField(max_length=20)
  member8 = models.CharField(max_length=20)
  member9 = models.CharField(max_length=20)
  member10 = models.CharField(max_length=20)

class Order(models.Model):
  team_name = models.CharField(max_length=20)
  enemy_name = models.CharField(max_length=20)
  single_6 = models.CharField(max_length=20)
  double_6_1 = models.CharField(max_length=20)
  double_6_2 = models.CharField(max_length=20)
  double_5 = models.CharField(max_length=20)
  double_5_1 = models.CharField(max_length=20)
  double_5_2 = models.CharField(max_length=20)
  double_4 = models.CharField(max_length=20)