from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.todos, name='todos-contactos'),
    path('crear/', views.crear, name='crear-contactos'),
    path('actualizar/<str:nombre>', views.actualizar, name='actualizar-contactos'),
    path('eliminar/<str:nombre>', views.eliminar, name='eliminar-contactos'),
    path('ver/<str:nombre>', views.ver, name='ver-contactos'),
    path('guardar/', views.guardar, name='guardar-contactos'),
]
