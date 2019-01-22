from django.conf.urls import url
from unodosmattress import views
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^dashboard$', views.dashboard, name = "dashboard"),
    url(r'^managepatients/$', views.managepatients, name="managepatients"),
    url(r'^managebeds/$', views.managebeds, name="managebeds"),
    url(r'^reports/$', views.reports, name="reports"),
    url(r'^viewpatients/$', views.viewpatients, name="viewpatients"),
    # path('/viewpatients/<int:idPatient/', views.viewpatients, name="viewpatients"),
    url(r'^ajax/addPatient/$', views.ajaxAddPatient, name="ajaxAddPatient"),
    url(r'^ajax/displayDoctors/$', views.ajaxDisplayDoctors, name="ajaxDisplayDoctors"),
    url(r'^ajax/getAvailableBeds/$', views.ajaxGetAvailableBeds, name="ajaxGetAvailableBeds"),
    url(r'^ajax/ajaxGetPatients/$', views.ajaxGetPatients, name="ajaxGetPatients"),

    #api
    url(r'^temperature/$', views.TemperatureList.as_view(), name='temperature-list'),
    url(r'^temperature/(?P<pk>[0-9]+)/$', views.TemperatureDetail.as_view(), name='temperature-detail'),
    url(r'^heartrate/$', views.HeartRateList.as_view(), name='heartRate-list'),
    url(r'^heartrate/(?P<pk>[0-9]+)/$', views.HeartRateDetail.as_view(), name='heartRate-detail'),
    url(r'^beds/$', views.BedList.as_view(), name='bed-list'),
    url(r'^beds/(?P<pk>[0-9]+)/$', views.BedDetail.as_view(), name='bed-detail'),
]
