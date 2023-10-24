from django.urls import path
from django.shortcuts import render
from AppCoder.views import curso

urlpatterns = [
    path('curso/',curso,name='curso')
]