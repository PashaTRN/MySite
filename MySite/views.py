from django.http import HttpResponse
from django.shortcuts import render 

def Home(request):
	return render (request,'Home.html')

def about(requst):
	return HttpResponse('It"s about')

def revers(request):
	text_revers = request.GET['usertext']
	return render (request,'revers.html', {'usertext':text_revers})