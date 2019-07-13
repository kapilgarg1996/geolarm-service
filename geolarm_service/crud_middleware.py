from django.http import JsonResponse

def Get(view):
	def get(request):
		if request.method == 'GET':
			return view(request)
		return JsonResponse({'error': 'Method not allowed'})
	return get