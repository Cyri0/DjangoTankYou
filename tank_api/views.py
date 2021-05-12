from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tank_logic.models import TankEvent
from .serializers import TankEventSerializer
from tank_logic import calculations

@api_view(['GET'])
def helper(request):
    api_urls = {
        'tankapi/':'API map',
        'tankapi/events/':'Return the tank events',
        'tankapi/average/':'Return the average fuel use in 100 km',
        'tankapi/sum_price/':'Return the summed price in HUF'
    }
    return Response(api_urls)

@api_view(['GET'])
def events(request):
    events = TankEvent.objects.all()
    serializer = TankEventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def average(request):
    events = TankEvent.objects.all().order_by('-date')
    average = {
        'average_consumption': calculations.calculate_consumption(events),
        'fuel_unit':'liter',
        'distance': 100,
        'distance_unit': 'kilometer'
    }
    return Response(average)

@api_view(['GET'])
def sum_price(request):
    sprice = {
        'summed_price': calculations.sum_price(TankEvent.objects.all()),
        'currency': 'HUF'
    }
    return Response(sprice)