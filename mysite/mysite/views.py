from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
	now = datetime.datetime.now()
	return render(request, 'home.html', {'current_date': now})

def selection(request):
	return render(request, 'select.html')

def weather(request):
	return render(request, 'weather.html', {'province':'ON', 'city':'TORONTO'})

