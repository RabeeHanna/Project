from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
	now = datetime.datetime.now() + datetime.timedelta(hours = 1)
	return render(request, 'home.html', {'current_date': now})

def hello(request):
	return HttpResponse("Page under construction")

