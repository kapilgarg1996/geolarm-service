from django.urls import path

from . import views

urlpatterns = [
	path('log', views.LogView.as_view(), name='log')
]