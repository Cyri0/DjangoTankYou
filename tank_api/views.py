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
        'tankapi/average/':'Return the average fuel use in 100 km'
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
    km = calculations.calculate_consumption(events)

    average = {
        'average_litre_per_hundred_km': km
    }
    return Response(average)