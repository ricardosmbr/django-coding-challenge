from django.contrib import admin
from .models import License, Client

class LicenseAdmin(admin.ModelAdmin):

    list_display = ('client','package','license_type','created_datetime','expiration_datetime')
    search_fields = ['client','package']

admin.site.register(License,LicenseAdmin)

class ClientAdmin(admin.ModelAdmin):

    list_display = ('client_name','poc_contact_name','poc_contact_email','admin_poc')
    search_fields = ['client_name']

admin.site.register(Client,ClientAdmin)