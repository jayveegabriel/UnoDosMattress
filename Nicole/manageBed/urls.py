"""thes1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from manageBed import views
from . models import  *

urlpatterns = [
    url(r'^save/$', views.save, name='save'),
	url(r'^addPatient/$', views.addPatient, name='addPatient'),
    url(r'^displayDoctors/$', views.displayDoctors, name='displayDoctors'),
    url(r'^addDoctor/$', views.addDoctor, name='addDoctor'),
    url(r'^getData/$', views.getData, name='getData'),
    url(r'^listOfPatients/$', views.listOfPatients, name='listOfPatients'),
    url(r'^listOfPatients/(?P<patient_id>[0-9]+)/$$', views.viewProfile, name='viewProfile'),
    url(r'^listOfDoctors/$', views.listOfDoctors, name='listOfDoctors'),
    url(r'^listOfDoctors/(?P<doctor_id>[0-9]+)/$$', views.viewDrProfile, name='viewDrProfile'),
    url(r'^reportListOfPatients/$', views.reportListOfPatients, name='reportListOfPatients'),
    url(r'^reportListOfPatients/(?P<patient_id>[0-9]+)/$$', views.heartRateReport, name='reportListOfPatients'),
    url(r'^heartRateReport/(?P<patient_id>[0-9]+)/$$', views.heartRateReport, name='heartRateReport'),
    url(r'^admin/$', admin.site.urls),
]
	