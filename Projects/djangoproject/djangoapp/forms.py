from django import forms 
from .models import *

class Studeinfoform(forms.ModelForm):
    class Meta:
        model = Studeinfo
        fields = '__all__'