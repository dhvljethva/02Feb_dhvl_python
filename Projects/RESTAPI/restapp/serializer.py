from rest_framework import serializers
from .models import *

class studserial(serializers.ModelSerializer):
    class Meta:
        model = Studinfo
        fields = '__all__'
        
