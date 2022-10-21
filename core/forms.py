from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

CHOICES= [
    ('SYS', 'SYS'),
    ('SE1', 'SE1'),
    ('SE2', 'SE2'),
    ('SE3', 'SE3'),
    ('SE4', 'SE4'),
    ('FI', 'FI'),
    ('DK1', 'DK1'),
    ('DK2', 'DK2'),
    ('Oslo', 'Oslo'),
    ('Kr_sand', 'Kr_sand'),
    ('Bergen', 'Bergen'),
    ('Molde', 'Molde'),
    ('TR_heim', 'TR_heim'),
    ('Tromso', 'Tromso'),
    ('EE', 'EE'),
    ('LV', 'LV'),
    ('AT', 'AT'),
    ('BE', 'BE'),
    ('DE_LU', 'DE_LU'),
    ('FR', 'FR'),
    ('NL', 'NL'),
    ]


class DeviceForm(forms.ModelForm):
    region = forms.CharField(label='Select the region', widget=forms.Select(choices=CHOICES))
    class Meta:
        model = Device
        fields = ['deviceID', 'region','mqttuser', 'mqttpass']


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		if commit:
			user.save()
		return user

class SearchForm(forms.Form):
	time = forms.IntegerField()	