from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from API.serializers import SensorsSerial,ImageSerializer,HeightSerializer
from API.models import Sensors,Image,Command,Height
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import login, authenticate,get_user_model, logout
from API.ai import predict
from API.plant import get_image
from django.urls import reverse
import json
from API.form import UploadForm
from API.models import FileUpdate
from django.shortcuts import get_object_or_404

class UpdateFirmwareView(View):
	def get(self, request, *args, **kwargs):
		files = FileUpdate.objects.order_by('-id').first()
		if files:
			file_object = get_object_or_404(FileUpdate, id=files.id)
			file_data = file_object.file
			response = HttpResponse(file_data, content_type='application/octet-stream')
			response['Content-Disposition'] = 'attachment; filename="%s"' % 'test.json'
			return response
		else:
			return HttpResponse("No current file")
		
class UploadFileView(View):
	def get(self, request):
		data = {
			'form': UploadForm()
		}
		return render(request, 'upload.html', data)
	def post(self, request):
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect(reverse('upload-update'))
		else:
			data = {
				'form': form
			}
			return render(request, 'upload.html', data)

class Irrigate(View):
	def get(self,request):
		datas = Command.objects.get(id=1)
		data={
			'dat':datas,
		}
		return render(request,'irrigate.html',data)
	def post(self,request):
		maxmum = request.POST.get('maxmum')
		minimum = request.POST.get('minimum')
		try:
			cmd = request.POST.get('cmd')
			dt = Command.objects.get(id=1)
			if(dt.cmd == True):
				dt.cmd = False
			else:
				dt.cmd = cmd
			dt.save()
			return HttpResponse(1)
		except:
			return HttpResponse(2)

		try:
			data = Command.objects.get(id=1)
			data.mH = maxmum
			data.mL = minimum
			data.save()

			return HttpResponse(1)
		except:
			return HttpResponse(3)

class Growth(View):
	def get(self,request):
		images = Height.objects.all().order_by('-id')
		data = {
			'images':images
		}
		return render(request,'growth.html',data)
		
class Photos(View):
	def get(self, request):
		images = Image.objects.all().order_by('-id')
		data = {
			'images':images,
		}
		return render(request,'photos.html',data)

	def post(self,request):
		cmd = request.POST.get('cmd')
		return HttpResponse(1)

class IndexView(View):
	def get(self,request):
		if(request.user.is_authenticated != True):
			return redirect('/login')
		sensor = Sensors.objects.last()
		allSensors = Sensors.objects.all()
		data = {
			'sensor':sensor,
			'allSensors':allSensors,
		}
		return render(request, "index.html", data)


class Login(View):
	def get(self, request):
		data = {}
		return render(request,"pages-login.html",data)

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		try:
			login(request,user)
			return HttpResponse(1)
		except:
			return HttpResponse("failed to login")

class PlantHeight(APIView):
	def get(self,request, *args, **kwargs):
		data = {
			"post":"Image",
			"url":"https://farmbotug.pythonanywhere.com/photo2/"
		}
		return Response(data)
	def post(self,request, *args, **kwargs):
		serializer = HeightSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			image = serializer.data['name'][1:]
			height, name = get_image(image)
			img = Height.objects.get(name=image[6:])
			img.height = height
			img.save()
			print(height)
			return Response({"height":height})
		else:
			return Response("Invalid")
		return Response("failure")
class ImageUpload(APIView):
	def get(self,request, *args, **kwargs):
		data = {
			'username':'kevin',
			'email':'babskevon@gmail.com'
		}
		return Response(data)

	def post(self,request, *args, **kwargs):
		serializer = ImageSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			image = serializer.data['name'][1:]
			data = predict(image)
			img = Image.objects.get(name=image[6:])
			print("/home/farmbotUg/hybrid/media/{}".format(img.name))
			print("kevin")
			if(data['stress'] != 'healthy' or data['bean'] != 'healthy'):
				img.predict = "{}/{}".format(data['bean'],data['stress'])
				img.bean_score = data['bean_score']
				img.stress_score = data['stress_score']
			else:
				img.predict = data['stress']
				img.bean_score = data['bean_score']
				img.stress_score = data['stress_score']
			img.save()
			# json.loads({'name':'kevin', 'data':"empty"})
			return Response(data)
			# return Response({'name':'kevin', 'data':"empty"})
		return Response(serializer.data)
		
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
			sensor = Sensors.objects.last()
			cmd = Command.objects.get(id=1)
			if(sensor.soil_moisture < cmd.mL):
				data = {'cmd':1}
			elif(sensor.soil_moisture >= cmd.mH):
				data = {'cmd':0}
			elif(cmd.cmd == True):
				data = {'cmd':1}
			else:
				data = {'cmd':0}
			return Response(data)
			
		return Response(serializer.errors)


class Signout(View):
	def get(self, request):
		logout(request)
		return redirect('/')