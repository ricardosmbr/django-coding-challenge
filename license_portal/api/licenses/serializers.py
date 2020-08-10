from rest_framework import serializers
from .models import License

class LicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = License
        fields = ('id','client', 'package' ,'license_type','created_datetime','expiration_datetime')
