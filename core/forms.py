from django import forms

from .models import *


FRUIT_CHOICES= [
    ('USA', 'USA'),
    ('EU', 'EU'),
    ('Asia', 'Asia'),
    ('Australia', 'Australia'),
    ]


class DeviceForm(forms.ModelForm):
    region = forms.CharField(label='Select the region', widget=forms.Select(choices=FRUIT_CHOICES))
    class Meta:
        model = Device
        fields = ['deviceID', 'region', 'setting', 'mqttuser', 'mqttpass']


