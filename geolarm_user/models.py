# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hashlib import md5
from django.db import models
import bcrypt

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