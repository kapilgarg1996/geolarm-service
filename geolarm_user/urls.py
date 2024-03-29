from django.urls import path

from . import views

urlpatterns = [
	path('login', views.UserLoginView.as_view(), name='login'),
	path('logout', views.UserLogoutView.as_view(), name='logout'),
	path('signup', views.UserSignupView.as_view(), name='signup'),
	path('get', views.UserView.as_view(), name='get')
]