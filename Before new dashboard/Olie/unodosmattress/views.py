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

position = ''

#Nurse
def dashboard(request):

	session_position = request.session.get('position','none')
	if session_position == "NURSE":
		patients = Patient.objects.values('idPatient')
		wew = []
		for x in range(0,len(patients)):
			obj = HeartRate.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').latest('date','time')
			obj2 = Temperature.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').latest('date','time')
			wew.append({"idPatient_id": patients[x]['idPatient'], "firstName":obj.idPatient.firstName, "lastName":obj.idPatient.lastName,"heartRate":obj.heartRate,"temperature":obj2.temperature, "bedNumber":obj.idPatient.bedNumber})

		context = {"patients_list": wew, 'position': request.session.get('position', 'none')}
		return render(request, 'dashboard/dashboard.html',context)
	return render(request, 'blocked.html')
#Nurse AJAX
def ajaxUpdateDashboard(request):

	patients = Patient.objects.values('idPatient')
	wew = []
	for x in range(0,len(patients)):
		obj = HeartRate.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').latest('date','time')
		obj2 = Temperature.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').latest('date','time')
		wew.append({"idPatient_id": patients[x]['idPatient'], "firstName":obj.idPatient.firstName, "lastName":obj.idPatient.lastName,"heartRate":obj.heartRate,"temperature":obj2.temperature, "bedNumber":obj.idPatient.bedNumber, "minTemp":obj.idPatient.minTemp, "maxTemp":obj.idPatient.maxTemp, "maxHeartRate":obj.idPatient.maxHeartRate, "minHeartRate":obj.idPatient.minHeartRate})
		print(obj)
	return JsonResponse (wew, safe=False)



def loginChecker (request):
	global position
	username = request.GET.get('username')
	password = request.GET.get('password')

	n = Employee.objects.filter(username=username).exists()
	d = Doctor.objects.filter(username=username).exists()

	#npass = Nurse.objects.filter(username=username).values('password')
	#dpass = Doctor.objects.filter(username=username).values('password')

	#print ("Nurse", npass)
	#print ("Doctor", dpass)

	if n == True or d == True:

		print(password)

		if  Employee.objects.filter(username=username,password=password).exists() or Doctor.objects.filter(username=username,password=password).exists():
			if Employee.objects.filter(username=username,password=password).exists():
				position = 'Nurse'
				request.session['position'] = "NURSE";
			else:
				position = "Doctor"
				request.session['position'] = "DOCTOR";
			data = {
				'is_match': True,
				'position': position,
			}

		else:
			data = {
				'is_match': False
			}
		print (data)

	else:
		data = {
			'is_existing': False
		}

	print (data)
	return JsonResponse(data)



#Nurse
def managepatients(request):

	session_position = request.session.get('position','none')
	if session_position == "NURSE":
		patients_list = Patient.objects.all()
		beds_list = Beds.objects.filter(bedStatus = "Available")
		doctors_list = Doctor.objects.all()

		context = {'patients_list': patients_list,'beds_list': beds_list, 'doctors_list': doctors_list}
		if request.method== 'POST':
			print(request.POST.get('firstname'))


		return render(request, 'dashboard/managepatients.html',context)
	return render(request, 'blocked.html')
#Nurse
def managebeds(request):

	session_position = request.session.get('position','none')
	if session_position == "NURSE":
		return render(request, 'dashboard/managebeds.html')
	return render(request, 'blocked.html')

#Nurse
def blocked(request):
	return render(request, 'blocked.html')

#Nurse
def reports(request):
	session_position = request.session.get('position','none')
	if session_position == "NURSE":
		return render(request, 'dashboard/reports.html')
	return render(request, 'blocked.html')
#Nurse
def viewpatients(request, idPatient):
	session_position = request.session.get('position','none')
	if session_position == "NURSE":
		p1 = Patient.objects.get(pk=idPatient)
		doctors = Patient_Doctors.objects.filter(Patient_id = idPatient).select_related('Patient').select_related('Doctor')
		context = {'patient':p1,'doctors':doctors}
		return render(request, 'dashboard/viewpatients.html',context)
	return render(request, 'blocked.html')
#Nurse AJAX
def ajaxDisplayDoctors(request):
	doctors = Doctor.objects.all()

	json_doctors = []

	for record in doctors:
		json_doctors.append({"idDoctor":record.idDoctor,"firstName":record.firstName})

	return JsonResponse (json_doctors, safe=False)

#Nurse AJAX
def ajaxGetAvailableBeds(request):
	beds = Beds.objects.filter(bedStatus="Available")

	beds_array = []

	for record in beds:
		beds_array.append({"idBeds":record.idBeds,"bedNumber":record.bedNumber})

	return JsonResponse (beds_array, safe=False)

#Nurse AJAX
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

	patient_var = Patient(firstName = firstName, middleName = middleName, lastName = lastName, birthDate = birthDate, religion = religion, minTemp = minTemp, maxTemp = maxTemp, minHeartRate = minHeartRate, maxHeartRate = maxHeartRate, contactNum = contactNum, bedNumber = bedNumber, status = "ON BED")
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

#---------------------API -------------------------------------
class TemperatureList(generics.ListCreateAPIView):
	queryset = Temperature.objects.all()
	serializer_class = TemperatureSerializer

class TemperatureDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Temperature.objects.all()
	serializer_class = TemperatureSerializer

class HeartRateList(generics.ListCreateAPIView):
	queryset = HeartRate.objects.all()
	serializer_class = HeartRateSerializer

class HeartRateDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = HeartRate.objects.all()
	serializer_class = HeartRateSerializer


class BedList(generics.ListCreateAPIView):
	queryset = Beds.objects.all()
	serializer_class = BedSerializer

class BedDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Beds.objects.all()
	serializer_class = BedSerializer


# class NotificationList(generics.ListCreateAPIView):
# 	queryset = Notification.objects.all()
# 	serializer_class = NotificationSerializer
#
# class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
# 	serializer_class = NotificationSerializer


#-------------------ADMIN ------------------------------
def manageusers(request):
	d1 = Doctor.objects.all()
	e1 = Employee.objects.all()
	users = []
	for x in range(0,len(d1)):

		users.append({'id':d1[x].pk, "username":d1[x].username,"firstName":d1[x].firstName, "middleName":d1[x].middleName, "lastName":d1[x].lastName, "userType":"Doctor"})

	for z in range(0, len(e1)):
		users.append({'id':e1[z].pk, "username":e1[z].username,"firstName":e1[z].firstName, "middleName":e1[z].middleName, "lastName":e1[z].lastName, "userType":e1[z].usertype})
	context = {"users_list": users}
	return render(request, 'admin/manageusers.html', context)

def managebeds(request):
	beds_list = Beds.objects.filter(bedStatus="Pending")
	context = {'beds_list': beds_list}
	return render(request, 'admin/managebeds.html',context)

def reports(request):
	return render(request, 'dashboard/reports.html')

def viewusers(request, username):
	d1 = Doctor.objects.filter(username=username).exists()
	e1 = Employee.objects.filter(username=username).exists()
	context = {}
	if d1 == True:
		doctor = Doctor.objects.get(username=username)
		context = {'user': doctor, 'usertype':'Doctor'}
	elif e1 == True:
		employee = Employee.objects.get(username=username)
		context = {'user': employee,'usertype':employee.usertype}
	print(context)
	return render(request, 'admin/viewusers.html', context)

def home(request):
	return render(request, 'admin/home.html')

def login(request):
	return render(request, 'login.html')


def logout(request):
	print("CLEAR SESSION")
	return render(request, 'login.html')

def ajaxSetBedAvailable(request):

	idBed = request.GET.get('id')
	bedNumber = request.GET.get('bedNumber')
	b1 = Beds.objects.get(idBeds = idBed)
	b1.bedStatus = "Available"
	b1.bedNumber = bedNumber
	b1.save()

	return HttpResponse()

def ajaxGetPendingBeds(request):

	beds = Beds.objects.filter(bedStatus="Pending")

	beds_array = []

	for record in beds:
		beds_array.append({"idBeds":record.idBeds,"bedNumber":record.bedNumber})

	return JsonResponse (beds_array, safe=False)


def ajaxCheckUser(request):

	#nurses= Nurse.objects.all()
	#doctors= Doctor.objects.all()

	#users = []

	#for user in nurses:
	#	users.append({"username": user.username})

	#for user in doctors:
	#	users.append({"username": user.username})

	#print(users)

	userType = request.GET.get('userType')
	print("userType", " ", userType)
	firstName = request.GET.get('firstName')
	middleName = request.GET.get('middleName')
	lastName = request.GET.get('lastName')
	contactNum = request.GET.get('contactNum')
	username = request.GET.get('username')
	password = request.GET.get('password')
	password2 = request.GET.get('password2')

	n = Employee.objects.filter(username=username).exists()
	d = Doctor.objects.filter(username=username).exists()

	print ("N", n)
	print ("D", d)

	if n == True or d == True:
		data = {
			'is_existing': True
		}

	else:
		data = {
				'is_existing': False
			}

	print(data)
	if userType == "Nurse" or userType == "Admin" and n == False:
		if password != password2:
			data = {
				'is_match': False
			}
		else:
			data = {
				'is_match': True
			}
			emp_var = Employee(firstName = firstName, middleName = middleName, lastName = lastName, contactNum = contactNum, username = username, password = password,usertype = userType)
			emp_var.save()
			print("YES SAVED NURSE")

	elif userType == "Doctor" and d == False:
		if password != password2:
			data = {
				'is_match': False
			}
		else:
			data = {
				'is_match': True
			}
			doctor_var = Doctor(firstName = firstName, middleName = middleName, lastName = lastName, contactNum = contactNum, username = username, password = password)
			doctor_var.save()
			print("YES SAVED DOCTOR")


	return JsonResponse(data)


def ajaxSaveNewPassword(request):
	id = request.GET.get('id')
	position = request.GET.get('position')
	password = request.GET.get('password')

	if position == "Doctor":
		u1 = Doctor.objects.get(pk=id)

	elif position == "Nurse":
		u1 = Employee.objects.get(pk = id)

	u1.password = password
	u1.save()


	return HttpResponse()

#---------------DOCTOR --------------------------
def patients(request):
		return render(request, 'doctor/patients.html')

def mypatients(request):
		return render(request, 'doctor/mypatients.html')


def reports(request):
	return render(request, 'doctor/reports.html')


def doctorhome(request):
	return render(request, 'doctor/home.html')
