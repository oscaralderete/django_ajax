from django.urls import path

from . import views

urlpatterns = [
	path('', views.forms, name='Forms'),
	path('ajax/', views.ajax, name='Ajax')
]
