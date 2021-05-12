from rest_framework import serializers
from tank_logic.models import TankEvent

class TankEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TankEvent
        fields = '__all__'