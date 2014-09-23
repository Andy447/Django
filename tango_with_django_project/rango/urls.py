from django.conf.urls import patterns, url #Patterns and urls are tools imported from django
from rango import views

urlpatterns = patterns('',  #Urlpatterns has to be the name of a tuple (list) that is used for mapping our urls. 
	url(r'^$', views.index, name ='index'), 
	#Urlpatterns tuple contains a series of calls to the django.conf.urls.url() which each handles a unique mapping. 
	#'^$' is an EMPTY string. Empty matching is useful here because Django only looks at the reminder of the url once the core url (ex. http://www.tangowithdjango.com/rango/) has been checked. So empty url here means just the url to http://www.tangowithdjango.com/rango/ so it's the index page.  
	#The second parameter means that views.index() method would be invoked by Django when the url matches. 
	#The view would pass a HttpRequest object as a parameter containing information about the user's request to the server
	#The third parameter of the url() function is optional for names in the form of a string. (index in this case)
	#A seperate URL file for each application is good practice to avoid coupling 
	url(r'^about/', views.about, name ='about'))