from django import forms
from manageBed.models import *

class PatientForm(forms.Form):
	firstName = forms.CharField()
	middleName = forms.CharField()
	lastName = forms.CharField()
	birthdate = forms.DateField()
	religion = forms.CharField()
	minTemp = forms.IntegerField()
	maxTemp = forms.IntegerField()
	minHeartRate = forms.IntegerField()
	maxHeartRate = forms.IntegerField()
	status = 1
	
	#class Meta:
	#	model = Patient
	#	fields = ('firstName','middleName','lastName','birthdate','religion','minTemp','maxTemp','minHeartRate','maxHeartRate','status')

