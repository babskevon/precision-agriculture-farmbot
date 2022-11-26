from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from API.serializers import SensorsSerial
from API.models import Sensors


class TestView(APIView):
	def get(self,request, *args, **kwargs):
		data = {
			'username':'kevin',
			'email':'babskevon@gmail.com'
		}

		return Response(data)

	def post(self,request, *args, **kwargs):
		serializer = SensorsSerial(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
			
		return Response(serializer.errors)