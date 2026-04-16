from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('profesional/', views.crear_profesional, name="crear_profesional"),
    path('servicio/', views.crear_servicio, name="crear_servicio"),
    path('entregable/', views.crear_entregable, name="crear_entregable"),
    path('buscar/', views.buscar_servicio, name="buscar_servicio"),
]
