# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hashlib import md5
from django.db import models
import bcrypt
from datetime import datetime

# Create your models here.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	dob = models.DateField()
	email = models.EmailField(unique=True, db_index=True)
	password = models.CharField(max_length=256)
	phone = models.CharField(max_length=16)
	city = models.CharField(max_length=64)
	state = models.CharField(max_length=64)
	country = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField()

	class Meta:
		db_table = 'users'

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.id:
			super(User, self).save(args, kwargs)
		self.password = bcrypt.hashpw(self.password, bcrypt.gensalt())
		super(User, self).save(args, kwargs)

	@classmethod
	def GetUser(cls, email, password):
		user = cls.objects.filter(email=email)[0]
		if bcrypt.checkpw(password, user.password):
			return user
		return None


class Session(models.Model)::
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(to='User')
	token = models.CharField(max_length=64, db_index=True)
	created_at = models.DateTimeField(auto_now_add=True)
	expiry_at = models.DateTimeField()

	class Meta:
		db_table = 'sessions'

	def __str__(self):
		return self.user.name

	def save(self, *args, **kwargs):
		self.token = bcrypt.hashpw(datetime.datetime.now().isoformat(), bcrypt.gensalt())
		super(Session, self).save(args, kwargs)

	@classmethod
	def Revive(cls, session):
		if session is not None:
			session.expiry_at = session.expiry_at + datetime.timedelta(days=1)
			session.save()
			return session
		return None

	@classmethod
	def IsExpired(cls, session):
		currentTime = datetime.now()
		if session.expiry_at < currentTime:
			return False
		return True
