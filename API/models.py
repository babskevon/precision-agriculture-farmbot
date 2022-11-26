from django.db import models

# Create your models here.
class Sensors(models.Model):
	light = models.CharField(max_length=10,blank=True)
	humidity = models.CharField(max_length=10,blank=True)
	temperature = models.CharField(max_length=10,blank=True)
	flowrate1 = models.CharField(max_length=10,blank=True,default=31.3)
	flowrate2 = models.CharField(max_length=10,blank=True,default=31.3)
	#flowrate2 = models.CharField(max_length=10,blank=True)
	soil_moisture = models.CharField(max_length=10,blank=True)
	distance = models.CharField(max_length=10,blank=True)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.soil_moisture

class Image(models.Model):
	name = models.ImageField(upload_to='API/static/garden_pic',null = True)
	create = models.DateTimeField(auto_now=True)

class Command(models.Model):
	cmd = models.BooleanField(default=False)
	mH = models.CharField(max_length=10,blank=True, default=80.0)
	mL = models.CharField(max_length=10, blank=True,default=30.0)