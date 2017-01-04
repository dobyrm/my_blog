from django.http import HttpResponse

def home(request):
	return HttpResponse("Hello, world. You're at the blog HOME index.")

def index(request):
	return HttpResponse("Hello, world. You're at the blog index.")
