from rest_framework import serializers
from .models import Sensors, Image

class SensorsSerial(serializers.ModelSerializer):
	class Meta:
		model = Sensors
		fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'