from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tankapi/', include('tank_api.urls')),
    path('tank/', include('tank_logic.urls'))
]