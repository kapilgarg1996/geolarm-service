from django.urls import path

from . import views

urlpatterns = [
	path('', views.HolidayView.as_view(), name='holiday')
]