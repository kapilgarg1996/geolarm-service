# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	dob = models.DateField()
	email = models.EmailField()
	password = models.CharField(max_length=256)
	phone = models.CharField(max_length=16)
	city = models.CharField(max_length=64)
	state = models.CharField(max_length=64)
	country = models.CharField(max_length=128)

	class Meta:
		db_table = 'users'

	def __str__(self):
		return self.name

class HolidayCalendar(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField(db_index=True)
	country = models.CharField(max_length=128)
	description = models.CharField(max_length=256)

	class Meta:
		db_table = 'holidays'

# Create your models here.
class Log(models.Model):
	id = models.AutoField(primary_key=True)
	latitude = models.FloatField()
	longitude = models.FloatField()
	day = models.CharField(max_length=16)
	date = models.DateField()
	time = models.TimeField()
	is_holiday = models.BooleanField()
	is_special_day = models.BooleanField()

	class Meta:
		db_table = 'logs'