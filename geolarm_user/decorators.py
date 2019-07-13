from .models import User

def authenticate_user(view_method):
	def authenticator(self, request, *args, **kwargs):
		user = User.GetUser(request.POST.email, request.POST.password)
		if user is not None:
			request.user = user
			request.is_authenticated = True
		return view_method(self, request, *args, **kwargs)

	return authenticator