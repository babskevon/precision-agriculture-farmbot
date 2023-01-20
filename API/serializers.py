from rest_framework import serializers
from API.models import Sensors, Image, Height

class SensorsSerial(serializers.ModelSerializer):
	class Meta:
		model = Sensors
		fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'



    
class HeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Height
        fields = '__all__'