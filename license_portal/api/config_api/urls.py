from django.contrib import admin
from django.urls import path
from licenses import views

urlpatterns = [
	path('', views.home, name ="home"),
	path('fourmonths/', views.MonthView, name ="four months"),
	path('monday/', views.MondayView, name ="monday"),
	path('week/', views.WeekView, name ="week"),
	path('allabove/', views.AllaboveView, name ="allabove"),
]
