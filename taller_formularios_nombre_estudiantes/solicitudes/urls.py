from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_solicitud, name='crear_solicitud'),
    path('confirmacion/', views.confirmacion_solicitud, name='confirmacion_solicitud'),
]
