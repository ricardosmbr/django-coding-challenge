from django.shortcuts import render
from django.http import HttpResponse
from .models import License, Package
from .notifications import EmailNotification
from datetime import datetime, timezone

# Create your views here.
def home(request):

	package = {
		0:'javascript_sdk',
		1:'ios_sdk',
		2:'android_sdk'
	}
	licenseType = {
		0:'production',
		1:'evaluation'
	}

	license = License.objects.all()
	license1 = []
	license2 = []
	license3 = []
	license4 = []
	List = set()

	today = datetime.now(timezone.utc)
	#returns day of the week
	weekday = today.weekday() 
	for x in license:
		code = 0
		dif = x.expiration_datetime - today
		if(dif.days == 120):
			code = 120
		if(dif.days < 30 and weekday == 0 and dif.days > 0):
			code = 30
		if(dif.days < 7 and dif.days > 0):
			code = 7
		if(code == 120):
			license1.append(x)
			license4.append(x)
		if(code == 30):
			license2.append(x)
			license4.append(x)
		if(code == 7):
			license3.append(x)
			license4.append(x)

		List.add(x.client.id)

	# send email
	template_name_mail = 'email.html'
	subject = 'about licenses'
	for i in List:
		body = {}
		context_mail = {}
		text = ""
		cont = 0
		for f in license1:
			if(i == f.client.id):
				text = "id: "+str(f.id)+" type: "+text+licenseType[f.license_type]+" package name: "+text+package[f.package]
				text = text+" expiration date: "+str(f.expiration_datetime)
				body["cli_name"] = f.client.client_name
				body["mail"] = f.client.poc_contact_email
				context_mail[cont] = text
	
		for f in license2:
			if(i == f.client.id):
				text = text+"id: "+str(f.client.id)+" type: "+licenseType[f.license_type]+" package name: "+package[f.package]
				text = text+" expiration date: "+str(f.expiration_datetime)
				body["cli_name"] = f.client.client_name
				body["mail"] = f.client.poc_contact_email
				context_mail[cont] = text
		for f in license3:
			if(i == f.client.id):
				text = text+"id: "+str(f.client.id)+" type: "+licenseType[f.license_type]+" package name: "+package[f.package]
				text = text+" expiration date: "+str(f.expiration_datetime)
				body["cli_name"] = f.client.client_name
				body["mail"] = f.client.poc_contact_email
				context_mail[cont] = text
		body["id"] = context_mail
		cont = cont + 1
		EmailNotification(subject,template_name_mail,body,[body["mail"]])

	# print(render(request,"email.html"))
	# mail.send_notification(List)
	print(type(context_mail))
	print(type(package))
	template_name = 'base.html'
	context = {}
	if request.method == 'POST':
		context = {
			'license':license4,
			'license1':license1,
			'license2':license2,
			'license3':license3,
			'package':package,
			'licenseType':licenseType
		}

	return render(request,template_name,context)