from django.shortcuts import render, redirect
from .models import TankEvent, ServiceEvent, PETROL_CHOICES, PETROL_STATION_CHOICES
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
    
    events = list(TankEvent.objects.all().order_by('-date'))
    events += list(ServiceEvent.objects.all().order_by('-date'))

    events.sort(key=lambda x: x.date, reverse=True)

    context = {
        'events':events,
    }
    return render(request, 'tank/history.html', context)

def stat(request):
    tank_events = TankEvent.objects.all().order_by('-date')

    events = list(TankEvent.objects.all().order_by('-date'))
    events += list(ServiceEvent.objects.all().order_by('-date'))

    context = {
        'last': calculations.getElementFromEvents(tank_events, 0),
        'consumption': calculations.calculate_consumption(tank_events),
        'average_quantity':calculations.calculate_average_quantity(tank_events),
        'average_price': calculations.calculate_average_price(tank_events),
        'sum_price': calculations.sum_price(events),
    }

    return render(request, 'tank/stat.html', context)

def service(request):
    return render(request, 'tank/service.html')

def save_service(request):
    if(request.method == 'POST'):
        km = request.POST['km']
        note = request.POST['note']
        price_ft = request.POST['price_ft']

        new_sevice_event = ServiceEvent(
            km = km,
            note = note,
            price_ft = price_ft
        )
        new_sevice_event.save()
        return redirect('history-view')
    return redirect('service-view')