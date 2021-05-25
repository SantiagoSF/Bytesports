from django.db import models


# Create your models here.

class Match(models.Model):
	team_name = models.CharField(max_length=20)
	field_name = models.CharField(max_length=20)
	max_players = models.IntegerField()
	match_hour = models.CharField(max_length=6)
	location_field = models.CharField(max_length=50)
	team_vs = models.CharField(max_length=50)