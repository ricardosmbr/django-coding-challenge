from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, timezone
from .models import License, Package
from . serializers import LicenseSerializer


@api_view(['GET'])
def home(request):
	urls ={}
	base = "http://127.0.0.1:8081/"
	urls['The client has licenses which expire in exactly 4 months'] = base+"fourmonths/"
	urls['The client has licenses which expire within a month and today is monday'] = base+"monday/"
	urls['The client has licenses which expire within a week'] = base+"week/"
	urls['All of the above'] = base+"allabove/"
	return Response(urls)

@api_view(['GET'])
def MonthView(request):
	today = datetime.now(timezone.utc)
	"""returns day of the week"""
	weekday = today.weekday() 
	license = []
	if request.method == 'GET':
		obj = License.objects.all()
		for x in obj:
			dif = x.expiration_datetime - today
			if(dif.days == 120):
				license.append(x)
		serializer = LicenseSerializer(license, many=True)	

		return Response(serializer.data)

@api_view(['GET'])
def MondayView(request):
	today = datetime.now(timezone.utc)
	"""returns day of the week"""
	weekday = today.weekday() 
	license = []
	if request.method == 'GET':
		obj = License.objects.all()
		for x in obj:
			dif = x.expiration_datetime - today
			if(dif.days < 30 and weekday == 0 and dif.days > 0):
				print(dif.days,weekday)
				license.append(x)
		serializer = LicenseSerializer(license, many=True)
		return Response(serializer.data)	

@api_view(['GET'])
def WeekView(request):
	today = datetime.now(timezone.utc)
	"""returns day of the week"""
	weekday = today.weekday() 
	license = []
	if request.method == 'GET':
		obj = License.objects.all()
		for x in obj:
			dif = x.expiration_datetime - today
			if(dif.days < 7 and dif.days > 0):
				license.append(x)
		serializer = LicenseSerializer(license, many=True)
		return Response(serializer.data)	

@api_view(['GET'])
def AllaboveView(request):
	today = datetime.now(timezone.utc)
	"""returns day of the week"""
	weekday = today.weekday() 
	license = []
	if request.method == 'GET':
		obj = License.objects.all()
		for x in obj:
			dif = x.expiration_datetime - today
			if(dif.days  == 120 or dif.days < 30 ):
				license.append(x)
		serializer = LicenseSerializer(license, many=True)

		return Response(serializer.data)