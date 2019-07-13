# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotAllowed, HttpResponseForbidden, HttpResponse, JsonResponse

from .models import User
from .decorators import authenticate_user

# Create your views here.
class UserView(View):
	def get(self, request):
		return HttpResponse(request.user)

	@authenticate_user
	def dispatch(self, request, *args, **kwargs):
		return super(UserView, self).dispatch(request, *args, **kwargs)

class UserLoginView(View):
	def post(self, request):
		email = request.POST['email']
		password = request.POST['password']
		user = User.GetUser(email, password)
		if user is not None:
			session = Session()
			session.user = user
			session.created_at = datetime.datetime.now()
			session.expiry_at = session.created_at+datetime.timedelta(days=1)
			session.save()
			data = {}
			data['user'] = user
			response = JsonResponse(data)
			response.set_cookie('t', value=session.token)
			return response
		return HttpResponseForbidden()

class UserLogoutView(View):
	def post(self, request):
		if request.user is not None:
			request.session.delete()
			response = HttpResponse('Success')
			response.set_cookie('t', '', expires=datetime.datetime.now()+datetime.timedelta(minutes=5))
			return response
		return HttpResponseForbidden()

	@authenticate_user
	def dispatch(self, request, *args, **kwargs):
		return super(UserLogoutView, self).dispatch(request, *args, **kwargs)

class UserSignupView(View):
	def post(self, request):
		user = User(**request.POST.dict())
		is_valid = User.Validate(user)
		if is_valid:
			session = Session()
			session.user = user
			session.created_at = datetime.datetime.now()
			session.expiry_at = session.created_at+datetime.timedelta(days=1)
			session.save()
			data = {}
			data['user'] = user
			response = JsonResponse(data)
			response.set_cookie('t', value=session.token)
			return response
		return HttpResponseForbidden()