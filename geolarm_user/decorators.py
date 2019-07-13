from .models import User, Session
from django.http import HttpResponseForbidden

def authenticate_user(view_method):
	def authenticator(self, request, *args, **kwargs):
		session = Session.objects.filter(token=request.COOKIES['t'])[0]
		if Session.IsExpired(session):
			return HttpResponseForbidden()
		request.user = session.user
		request.is_authenticated = True
		Session.Revive(session)
		response = view_method(self, request, *args, **kwargs)
		if response.status_code is 200:
			response.set_cookie('t', value=session.token, expires=session.expiry_at)
		return response

	return authenticator