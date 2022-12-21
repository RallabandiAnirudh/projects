from rest_framework import serializers
from .models import *



class Clinicserializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields='__all__'

