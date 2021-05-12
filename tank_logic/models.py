from django.db import models
from datetime import date
from django.db import models
from datetime import date

PETROL_CHOICES = (
    ('gasoline95', '95-ös benzin'),
    ('gasoline100', '100-as benzin'),
    ('diesel', 'dízel'),
)

PETROL_STATION_CHOICES = (
    ('mol', 'MOL'),
    ('shell', 'Shell'),
    ('omv', 'OMV')
)

class TankEvent(models.Model):
    km = models.IntegerField(default=0)
    petrol_type = models.CharField(max_length=20, choices=PETROL_CHOICES, default='gasoline95')
    petrol_station = models.CharField(max_length=20, choices=PETROL_STATION_CHOICES, default='mol')
    petrol_quantity_liter = models.FloatField(default=0.0)
    price_ft = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return (f'{self.km} - {self.date}')