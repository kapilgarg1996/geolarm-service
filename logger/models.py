# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Log(models.Model):
	id = models.AutoField(primary_key=True)
	latitude = models.FloatField()
	longitude = models.FloatField()
	day = models.CharField(max_length=16)
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)
	is_holiday = models.BooleanField()
	is_special_day = models.BooleanField()

	class Meta:
		db_table = 'logs'