from django.http import HttpResponse 

def index(request):
	return HttpResponse('<b>Rango & Andy says hello world!</b> <br> <a href="/rango/about">About</a>') #Each view must return a Http Response object sent to the client requesting the view

def about(request):
	return HttpResponse('Rango & Andy says: Here is the about page. <br> <a href="/rango/">Back to Index</a>') 	