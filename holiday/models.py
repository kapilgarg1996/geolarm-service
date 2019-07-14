# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HolidayCalendar(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField(db_index=True)
	country = models.CharField(max_length=128)
	description = models.CharField(max_length=256)

	class Meta:
		db_table = 'holidays'

	@classmethod
	def IsHoliday(cls, date, country='IN'):
		holidays = cls.objects.filter(date=date, country=country)
		if holidays.count() >= 1:
			return holidays
		return None