from django.db import models
from datetime import date
from django.db.models.signals import post_save
from colors.fields import ColorField
from django import forms

# Create your models here.

class Station(models.Model):
	name = models.CharField(max_length=200)
	latitude = models.FloatField() 
	longitude = models.FloatField()
	elevation = models.FloatField()
	def __unicode__(self):
		return "%s (%s,%s)"%(self.name,self.latitude,self.longitude)
	class Meta:
        	ordering = ['name']

class ColorChoiceField(models.CharField):
	pass
class Choice(models.Model):
   	name = models.CharField(max_length=200)
	color = ColorChoiceField( max_length=7)
	details = models.CharField(max_length=200)	
	weight = models.IntegerField()	
	def __unicode__(self):
		return self.name
	class Meta:
		ordering = ['-id']


HOUR_CHOICES = (
	(0,'00'),(1,'01'),(2,'02'),
	(3,'03'),(4,'04'),(5,'05'),
	(6,'06'),(7,'07'),(8,'08'),
	(9,'09'),(10,'10'),(11,'11'),
	(12,'12'),(13,'13'),(14,'14'),
	(15,'15'),(16,'16'),(17,'17'),
	(18,'18'),(19,'19'),(20,'20'),
	(21,'21'),(22,'22'),(23,'23'),
) 

class Evaluation(models.Model):
	station = models.ForeignKey(Station)
	choice = models.ForeignKey(Choice)
	date = models.DateField('Date')
	hour = models.IntegerField(choices=HOUR_CHOICES)

	def save(self, *args, **kwargs):
		super(Evaluation, self).save(*args, **kwargs)

	def __str__(self):
	
		return '%s %s %s %s' % (self.station.name, self.choice.name,self.date,self.hour)
	class Meta:
		unique_together = ('station','date','hour') 

def keep_alive(sender,**kwargs):
	pass
post_save.connect(keep_alive, sender=Evaluation)
