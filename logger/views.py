# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views import View
from geolarm_service import Get

# Create your views here.
class LogView(View):
	def get(self, request):
		return HttpResponse('Here are your logs')