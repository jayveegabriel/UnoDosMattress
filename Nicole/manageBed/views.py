from django.shortcuts import render
from django.http import HttpResponse
from . models import  *
from manageBed.forms import PatientForm
from datetime import datetime
from django.http import JsonResponse
from django.core import serializers
from django.utils.dateparse import parse_date

# Create your views here.

def addPatient(request):

	return render(request, 'addPatient.html')

def displayDoctors(request):
	doctors = Doctor.objects.all()

	json_doctors = []

	for record in doctors:
		json_doctors.append({"idDoctor":record.idDoctor,"firstName":record.firstName})

	return JsonResponse (json_doctors, safe=False)

def save(request): 

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
	age = (datetime.now().date() - bday).days / 365.25

	doctors = request.GET.getlist('doctors[]')
	print(firstName,middleName,lastName,birthDate,religion,minTemp,maxTemp,minHeartRate,maxHeartRate,contactNum,bedNumber)
	print(doctors)

	patient_var = Patient(firstName = firstName, middleName = middleName, lastName = lastName, birthDate = birthDate, age = age, religion = religion, minTemp = minTemp, maxTemp = maxTemp, minHeartRate = minHeartRate, maxHeartRate = maxHeartRate, contactNum = contactNum, bedNumber = bedNumber, status = 1)
	patient_var.save()

	patient_id = Patient.objects.filter(bedNumber=bedNumber).values('idPatient')
	print(patient_id)
    
	for doctor in range(0,len(doctors)): 

		print (doctor)
		patient_doctors = Patient_Doctors(patientNumber=patient_id[0]['idPatient'],doctorsID=doctors[doctor])
		patient_doctors.save()

	return render(request, 'addPatient.html')	

def addDoctor(request):

	if request.method == "POST":
		print("doctor")
		firstName = request.POST.get('firstName')		
		middleName = request.POST.get('middleName')
		lastName = request.POST.get('lastName')
		contactNum = request.POST.get('contactNum')
		username = request.POST.get('username')
		password = request.POST.get('password')

		doctor_var = Doctor(firstName = firstName, middleName = middleName, lastName = lastName, contactNum = contactNum, username = username, password = password)
		doctor_var.save()

	return render(request, 'addDoctor.html')

def listOfPatients(request):

	list_of_patient = Patient.objects.values('idPatient','firstName','lastName')
	print(list_of_patient)
	context = {'list_of_patient':list_of_patient}

	return render(request,'listOfPatients.html',context)

def viewProfile(request, patient_id):
	print(patient_id)

	patient_profile = Patient.objects.filter(idPatient=patient_id).values('idPatient','firstName','lastName','middleName','birthDate','age','religion','minTemp','maxTemp','minHeartRate','maxHeartRate','status')
	context = {'patient_profile':patient_profile}

	if request.method == "POST":
		idStatus = request.POST.get('status')
		print(idStatus)
		patient_profile.update(status=idStatus)
#otherwaytoupdate		Patient.objects.filter(idPatient=patient_id).update(status=idStatus)
	return render(request, 'viewProfile.html',context)

def listOfDoctors(request):

	list_of_doctors = Doctor.objects.values('idDoctor','firstName','lastName')
	print(list_of_doctors)
	context = {'list_of_doctors':list_of_doctors}

	return render(request,'listOfDoctors.html',context)

def viewDrProfile(request, doctor_id):
	print(doctor_id)

	doctor_profile = Doctor.objects.filter(idDoctor=doctor_id).values('idDoctor','firstName','lastName','middleName','contactNum','username','password')
	context = {'doctor_profile':doctor_profile}

	if request.method == "POST":
		idStatus = request.POST.get('status')
		print(idStatus)
		patient_profile.update(status=idStatus)
#otherwaytoupdate		Patient.objects.filter(idPatient=patient_id).update(status=idStatus)
	return render(request, 'viewDrProfile.html',context)

def reportListOfPatients(request):

	list_of_patient = Patient.objects.values('idPatient','firstName','lastName')
	print(list_of_patient)
	context = {'list_of_patient':list_of_patient}

	return render(request,'reportListOfPatients.html',context)

def heartRateReport(request,patient_id):

	print(patient_id)
	patient_report = HeartRate.objects.filter(idPatient=patient_id).values('idPatient','heartRate','time','date')
	print(patient_report)
	context = {'patient_report':patient_report}

		#patientd_report = HeartRate.objects.filter(idPatient=patient_id,date=nDate,startTime=startTime).values('heartRate','time')

		#context={'patientd_report':patientd_report}
	return render(request,'heartRateReport.html',context)

def getData(request):

	idPatient = request.GET.get('id')
	date = request.GET.get('date')
	startTime = request.GET.get('startTime')
	endTime = request.GET.get('endTime')
	print(date)

	newDate = date.replace(".", "")
	finDate = newDate.replace(",", "")
	print(finDate)

	#date = datetime.strptime(finDate,'%b:%d:%Y').date()
	start = datetime.strptime(startTime, '%H:%M').time()
	end = datetime.strptime(endTime, '%H:%M').time()


	if startTime == '01:00':
		data = {
			'check': True
		}
	else:
		data = {
			'check': False
		}
	return JsonResponse(data)
