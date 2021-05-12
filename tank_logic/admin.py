from django.contrib import admin
from .models import TankEvent, ServiceEvent
# Register your models here.
admin.site.register(TankEvent)
admin.site.register(ServiceEvent)