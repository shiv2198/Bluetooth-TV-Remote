from django.db import models
#from django_mysql.models import JSONField
#from django.contrib.postgres.fields import ArrayField
# Create your models here.

'''
class Broadcaster:
	def __init__(self,Airtel,TataSky,GTPL,DishTV):
		self.Airtel=Airtel
		self.DishTV=DishTV
		self.GTPL=GTPL
		self.TataSky=TataSky

class BroadcasterField(models.Field):
	def __init__(self,*args,**kwargs):
		kwargs['max_length']=100
		super().__init__(*args,**kwargs)

'''
class Time(models.Model):
	Name=models.CharField(max_length=100)
	Starting_time=models.TimeField(default=None)
	Ending_Time=models.TimeField(default=None)

	def __str__(self):
		return self.Name

class Distributor(models.Model):
	D_id=models.IntegerField(default=None)
	D_name=models.CharField(max_length=100)
	D_string=models.CharField(max_length=100)


	def __str__(self):
		return self.D_name


class Channel(models.Model):
	C_id=models.IntegerField(default=None)
	C_name=models.CharField(max_length=100)
	C_icon=models.FileField(null=True,blank=True)
	Airtel=models.IntegerField(null=True)
	GTPL=models.IntegerField(null=True)
	TataSky=models.IntegerField(null=True)
	DishTV=models.IntegerField(null=True)
	


	def __str__(self):
		return self.C_name



class Show(models.Model):
	S_id=models.IntegerField(default=None)
	S_name=models.CharField(max_length=100)
	S_icon=models.FileField(null=True,blank=True)
	D_name=models.CharField(max_length=100)
	C_name=models.CharField(max_length=100)
	Monday=models.ManyToManyField(Time,related_name='monday')
	Tuesday=models.ManyToManyField(Time,related_name='tueday')
	Wednesday=models.ManyToManyField(Time,related_name='wednesday')
	Thursday=models.ManyToManyField(Time,related_name='thursday')
	Friday=models.ManyToManyField(Time,related_name='friday')
	Saturday=models.ManyToManyField(Time,related_name='saturday')
	Sunday=models.ManyToManyField(Time,related_name='sunday')

	def __str__(self):
		return self.S_name

class Customer(models.Model):
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	emailid=models.EmailField(max_length=100,blank=True)
	mobileno=models.IntegerField(default=None,null=True,blank=True)
	distributor=models.CharField(max_length=100)

	def __str__(self):
		return self.username



