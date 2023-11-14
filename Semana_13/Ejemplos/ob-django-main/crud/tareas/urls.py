from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver, name='ver-tareas'),
    path('crear/', views.crear, name='crear-tareas'),
    path('guardar/', views.guardar, name='guardar-tareas'),
    path('actualizar/<int:id>/', views.actualizar, name='actualizar-tareas'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar-tareas'),
    path('detalles/<int:id>/', views.detalles, name='detalles-tareas'),
]
