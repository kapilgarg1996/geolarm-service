# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotAllowed, HttpResponseForbidden, HttpResponse

from .models import User
from .decorators import authenticate_user

# Create your views here.
class UserView(View):
	def get(self, request):
		if request.user is not None:
			return HttpResponse(request.user)

		return HttpResponseNotAllowed()

	@authenticate_user
	def dispatch(self, request, *args, **kwargs):
		return super(UserView, self).dispatch(request, *args, **kwargs)

class UserLoginView(View):
	def post(self, request):
		if request.user is not None:
			return HttpResponse(request.user)
		return HttpResponseForbidden()

	@authenticate_user
	def dispatch(self, request, *args, **kwargs):
		return super(UserLoginView, self).dispatch(request, *args, **kwargs)

class UserLogoutView(View):
	def post(self.request):
		if request.user is not None:
			return HttpResponse(request.user)
		return HttpResponseForbidden()

	@authenticate_user
	def dispatch(self, request, *args, **kwargs):
		return super(UserLogoutView, self).dispatch(request, *args, **kwargs)

class UserSignupView(View):
	def post(self.request):
		if request.user is not None:
			return HttpResponse(request.user)
		return HttpResponseForbidden()

	@authenticate_user
	def dispatch(self, request, *args, **kwargs):
		return super(UserSignupView, self).dispatch(request, *args, **kwargs)