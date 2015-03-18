from django.shortcuts import render

from django.http import HttpResponse
def index(request):
	return HttpResponse("Rango says Hello, World! ....<br/> <a href='/rango/about'>About</a> ")

def about(request):
	return HttpResponse("Rango says this is about page...<br /> <a href='/rango/'>Index</a>")