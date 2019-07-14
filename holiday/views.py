# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import json

from django.shortcuts import render
from django.views import View
from django.core import serializers
from django.http import HttpResponseNotFound, JsonResponse, HttpResponseBadRequest

from .models import HolidayCalendar
# Create your views here.
class HolidayView(View):
	def get(self, request):
		try:
			date = datetime.datetime.strptime(request.GET['date'], '%Y-%m-%d')
			country = request.GET.get('country', default='IN')
			holidays = HolidayCalendar.IsHoliday(date, country)
		except KeyError:
			return HttpResponseBadRequest('Date is missing')
		if holidays is not None:
			holidays = holidays.values('id', 'date', 'country', 'description')
			return JsonResponse(list(holidays), safe=False)
		return HttpResponseNotFound()

	def post(self, request):
		try:
			data = json.loads(request.body)
			date = datetime.datetime.strptime(data['date'], '%Y-%m-%d')
			description = data['description']
			country = data['country']
		except KeyError as e:
			return HttpResponseBadRequest('Data is missing: %s' % str(e))
		holiday = HolidayCalendar()
		holiday.date = date
		holiday.description = description
		holiday.country = country
		holiday.save()
		return JsonResponse({'message':'Success'})