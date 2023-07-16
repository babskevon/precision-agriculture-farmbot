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
	name = models.ImageField(upload_to='garden_pic',null = True)
	predict = models.CharField(default='healthy',max_length=150)
	bean_score = models.CharField(max_length=150,null=True)
	stress_score = models.CharField(max_length=150,null=True)
	create = models.DateTimeField(auto_now=True)

class Height(models.Model):
	name = models.ImageField(upload_to='height',null = True)
	height = models.CharField(max_length=150, null=True)
	create = models.DateTimeField(auto_now=True)

class Command(models.Model):
	cmd = models.BooleanField(default=False)
	mH = models.CharField(max_length=10,blank=True, default=80.0)
	mL = models.CharField(max_length=10, blank=True,default=30.0)


class FileUpdate(models.Model):
	file = models.FileField(upload_to='updates')
	created_at = models.DateTimeField(auto_now=True)
	current_update = models.BooleanField(default=False)
	version = models.CharField(default='1.0.0',max_length=20)
	message = models.TextField(blank=True, null=True)