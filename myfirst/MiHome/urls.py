from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('9:00', views.g_9_00),
    path('9:30', views.g_9_30),
    path('10:00', views.g_10_00),
    path('10:30', views.g_10_30),
    path('11:00', views.g_11_00),
    path('11:30', views.g_11_30),
    path('12:00', views.g_12_00),
    path('12:30', views.g_12_30),
    path('13:00', views.g_13_00),
    path('13:30', views.g_13_30),
    path('14:00', views.g_14_00),
    path('14:30', views.g_14_30),
    path('15:00', views.g_15_00),
    path('15:30', views.g_15_30),
    path('16:00', views.g_16_00),
    path('16:30', views.g_16_30),
    path('17:00', views.g_17_00),
    path('17:30', views.g_17_30),
]

