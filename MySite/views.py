from django.http import HttpResponse
from django.shortcuts import render 

def Home(requst):
	return render (requst,'Home.html')

def about(requst):
	return HttpResponse('It"s about')