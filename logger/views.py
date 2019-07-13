# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from geolarm_service import Get

# Create your views here.

def log(request):
	return HttpResponse("Hello, I will log everything")