from django.shortcuts import render, redirect
from .models import TankEvent, PETROL_CHOICES, PETROL_STATION_CHOICES
from . import calculations

def new_tank(request):
    if request.method=='POST':
        km = request.POST['km']
        petrol_type = request.POST['petrol_type']
        petrol_station = request.POST['petrol_station']
        petrol_quantity_liter = request.POST['petrol_quantity_liter']
        price_ft = request.POST['price_ft']
        new_event = TankEvent(
            km = km,
            petrol_type = petrol_type,
            petrol_station = petrol_station,
            petrol_quantity_liter = petrol_quantity_liter,
            price_ft = price_ft
        )
        new_event.save()
        return redirect('history-view')
    context =  {
        'petrol_types':PETROL_CHOICES,
        'petrol_stations':PETROL_STATION_CHOICES,
    }
    return render(request, 'tank/new_tank.html', context)

def history(request):

    events = TankEvent.objects.all().order_by('-date')
    context = {
        'events':events,
    }
    return render(request, 'tank/history.html', context)

def stat(request):
    events = TankEvent.objects.all().order_by('-date')
    context = {
        'last': calculations.getElementFromEvents(events, 0),
        'consumption': calculations.calculate_consumption(events),
        'average_quantity':calculations.calculate_average_quantity(events),
        'average_price': calculations.calculate_average_price(events),
        'sum_price': calculations.sum_price(events),
    }

    return render(request, 'tank/stat.html', context)

def service(request):
    return render(request, 'tank/service.html')