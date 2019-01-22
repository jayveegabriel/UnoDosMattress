from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import  *

from rest_framework import generics
from unodosmattress.serializers import TemperatureSerializer, BedSerializer, HeartRateSerializer

from rest_framework.response import Response
from rest_framework.reverse import reverse
from datetime import datetime
from django.http import JsonResponse
from django.core import serializers
from django.utils.dateparse import parse_date


# Create your views here.
def dashboard(request):
	return render(request, 'dashboard/dashboard.html')

def managepatients(request):

	patients_list = Patient.objects.all()
	beds_list = Beds.objects.filter(bedStatus = "Available")
	doctors_list = Doctor.objects.all()



	context = {'patients_list': patients_list,'beds_list': beds_list, 'doctors_list': doctors_list}
	if request.method== 'POST':
		print(request.POST.get('firstname'))


	return render(request, 'dashboard/managepatients.html',context)

def managebeds(request):
	return render(request, 'dashboard/managebeds.html')

def reports(request):
	return render(request, 'dashboard/reports.html')


def viewpatients(request):

	# patient = Patient.objects.get(pk=idPatient)

	return render(request, 'dashboard/viewpatients.html')

#Gets the doctor from db then return it for dropdown in managepatients.html
def ajaxDisplayDoctors(request):
	doctors = Doctor.objects.all()

	json_doctors = []

	for record in doctors:
		json_doctors.append({"idDoctor":record.idDoctor,"firstName":record.firstName})

	return JsonResponse (json_doctors, safe=False)

def ajaxGetAvailableBeds(request):
	beds = Beds.objects.filter(bedStatus="Available")

	beds_array = []

	for record in beds:
		beds_array.append({"idBeds":record.idBeds,"bedNumber":record.bedNumber})

	return JsonResponse (beds_array, safe=False)


def ajaxAddPatient(request):
	firstName = request.GET.get('firstName')
	middleName = request.GET.get('middleName')
	lastName = request.GET.get('lastName')
	birthDate = request.GET.get('birthDate')
	religion = request.GET.get('religion')
	minTemp = request.GET.get('minTemp')
	maxTemp = request.GET.get('maxTemp')
	minHeartRate = request.GET.get('minHeartRate')
	maxHeartRate = request.GET.get('maxHeartRate')
	contactNum = request.GET.get('contactNum')
	bedNumber = request.GET.get('bedNumber')

	bday = parse_date(birthDate)
	print(bday)
	# age = (datetime.now().date() - bday).days / 365.25

	doctors = request.GET.getlist('doctors[]')
	print(firstName,middleName,lastName,birthDate,religion,minTemp,maxTemp,minHeartRate,maxHeartRate,contactNum,bedNumber)
	print(doctors)

	patient_var = Patient(firstName = firstName, middleName = middleName, lastName = lastName, birthDate = birthDate, religion = religion, minTemp = minTemp, maxTemp = maxTemp, minHeartRate = minHeartRate, maxHeartRate = maxHeartRate, contactNum = contactNum, bedNumber = bedNumber, status = 1)
	patient_var.save()

	patient_bed = Patient_Table(idBeds_id=bedNumber, idPatient_id=patient_var.pk)
	patient_bed.save()

	for x in range(0, len(doctors)):
		patient_doctor = Patient_Doctors( Doctor_id = doctors[x], Patient_id = patient_var.pk)
		patient_doctor.save()

	bed = Beds.objects.get(pk = bedNumber)
	bed.bedStatus = "Occupied"
	bed.save()
	return HttpResponse()

def ajaxGetPatients(request):

	patients = Patient.objects.all()
	patients_array = []

	for record in patients:
		patients_array.append({"idPatient":record.idPatient,"firstName":record.firstName,"lastName":record.lastName,
		"middleName":record.middleName,"bedNumber":record.bedNumber,"status":record.status,})

	return JsonResponse (patients_array, safe=False)

class TemperatureList(generics.ListCreateAPIView):
	queryset = Temperature.objects.all()
	serializer_class = TemperatureSerializer

class TemperatureDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TemperatureSerializer

class HeartRateList(generics.ListCreateAPIView):
	queryset = HeartRate.objects.all()
	serializer_class = HeartRateSerializer

class HeartRateDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = HeartRateSerializer


class BedList(generics.ListCreateAPIView):
	queryset = Beds.objects.all()
	serializer_class = BedSerializer

class BedDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = BedSerializer
