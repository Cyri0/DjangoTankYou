
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.history, name='history-view'),
    path('new/', views.new_tank, name='new-tank-view'),
    path('stat/', views.stat, name="stat-view"),
    path('service/', views.service, name="service-view"),
    path('save_service/', views.save_service, name="save_service"),
]