from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.helper, name='api-helper'),
    path('events/', views.events, name='get-events'),
    path('average/', views.average, name='get-average')
]
