from django.conf.urls import url
from unodosmattress import views
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    url(r'^login/$', views.login, name = "login"),
    url(r'^ajax/loginChecker/$', views.loginChecker, name = "loginChecker"),
    url(r'^blocked/$', views.blocked, name = "blocked"),


    #nurse
    url(r'^dashboard/$', views.dashboard, name = "dashboard"),
    url(r'^managepatients/$', views.managepatients, name="managepatients"),
    url(r'^managebeds/$', views.managebeds, name="managebeds"),
    # url(r'^reports/$', views.reports, name="reports"),
    url(r'^viewpatients/(?P<idPatient>[0-9]+)/$', views.viewpatients, name="viewpatients"),
    # path('/viewpatients/<int:idPatient/', views.viewpatients, name="viewpatients"),
    url(r'^ajax/addPatient/$', views.ajaxAddPatient, name="ajaxAddPatient"),
    url(r'^ajax/displayDoctors/$', views.ajaxDisplayDoctors, name="ajaxDisplayDoctors"),
    url(r'^ajax/getAvailableBeds/$', views.ajaxGetAvailableBeds, name="ajaxGetAvailableBeds"),
    url(r'^ajax/ajaxGetPatients/$', views.ajaxGetPatients, name="ajaxGetPatients"),
    url(r'^ajax/ajaxUpdateDashboard/$', views.ajaxUpdateDashboard, name="ajaxUpdateDashboard"),


    #api
    url(r'^temperature/$', views.TemperatureList.as_view(), name='temperature-list'),
    url(r'^temperature/(?P<pk>[0-9]+)/$', views.TemperatureDetail.as_view(), name='temperature-detail'),
    url(r'^heartrate/$', views.HeartRateList.as_view(), name='heartRate-list'),
    url(r'^heartrate/(?P<pk>[0-9]+)/$', views.HeartRateDetail.as_view(), name='heartRate-detail'),
    url(r'^beds/$', views.BedList.as_view(), name='bed-list'),
    url(r'^beds/(?P<pk>[0-9]+)/$', views.BedDetail.as_view(), name='bed-detail'),
    # url(r'^notification/$', views.NotificationList.as_view(), name='notification-list'),
    # url(r'^notification/(?P<pk>[0-9]+)/$', views.NotificationDetail.as_view(), name='notification-detail'),



    #admin
    url(r'^$login/', views.login, name = "login"),
    url(r'^home/$', views.home, name = "home"),
    url(r'^admin/manageusers/$', views.manageusers, name="manageusers"),
    url(r'^admin/managebeds/$', views.managebeds, name="managebeds"),
    url(r'^viewusers/(?P<username>[\w\-]+)/$', views.viewusers, name="viewusers"),
    url(r'^ajax/setBedAvailable/$', views.ajaxSetBedAvailable, name="ajaxSetBedAvailable"),
    url(r'^ajax/getPendingBeds/$', views.ajaxGetPendingBeds, name="ajaxGetPendingBeds"),
    url(r'^ajax/checkUser/$', views.ajaxCheckUser, name="ajaxCheckUser"),
    url(r'^ajax/saveNewPassword/$', views.ajaxSaveNewPassword, name="ajaxSaveNewPassword"),


    #doctor

    url(r'^doctor/home/$', views.doctorhome, name="doctorhome"),
    url(r'^doctor/mypatients/$', views.mypatients, name="mypatients"),
    url(r'^doctor/reports/$', views.reports, name="reports"),
    url(r'^doctor/patients/$', views.patients, name="patients"),

    url(r'^logout/$', views.logout, name="logout"),



]
