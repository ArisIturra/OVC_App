from django.db import models
import datetime
from datetime import datetime
from time import strftime
from statistics.models import *


class Classification(models.Model):
	name  = models.CharField(max_length=50)
	short_name = models.CharField(max_length=50)
	details = models.TextField(blank=True)

	def __unicode__(self):
                return  '%s (%s)'%(self.name,self.short_name)
	class Meta:
		ordering = ['name']

 
class Location(models.Model):
	name  = models.CharField(max_length=50)
        latitude = models.FloatField(null=True,blank=True)
        longitude = models.FloatField(null=True,blank=True)
	
	def __unicode__(self):
                return  '%s'%(self.name)
	class Meta:
		ordering = ['name']


class MMIntegerField(models.IntegerField):
	"Min Max Integer Field - use in place of models.IntegerField"
	def __init__(self, verbose_name=None, min_value=None, max_value=None, **kwargs):
		self.min_value = min_value
		self.max_value = max_value
		models.IntegerField.__init__(self, verbose_name, **kwargs)
    
	def formfield(self, **kwargs):
		return models.IntegerField.formfield(self,  min_value=self.min_value, max_value=self.max_value, **kwargs)
    
	def get_internal_type(self):
		return "IntegerField"  


from datetime import date
class Seism(models.Model):
	event_date = models.DateField('Event Date')
	
	p_hh = MMIntegerField('P arrival HH',max_value=23,min_value=0) 
	p_mm = MMIntegerField('MM',max_value=59,min_value=0) 
	p_ss = MMIntegerField('SS',max_value=59,min_value=0) 
	p_ms = MMIntegerField('MS',max_value=999,min_value=0)
	
	s_hh = MMIntegerField('S arrival HH',max_value=23,min_value=0,null=True,blank=True) 
	s_mm = MMIntegerField('MM',max_value=59,min_value=0,null=True,blank=True) 
	s_ss = MMIntegerField('SS',max_value=59,min_value=0,null=True,blank=True) 
	s_ms = MMIntegerField('MS',max_value=999,min_value=0,null=True,blank=True) 
	
	c_hh = MMIntegerField('Coda HH',max_value=23,min_value=0,null=True,blank=True) 
	c_mm = MMIntegerField('MM',max_value=59,min_value=0,null=True,blank=True) 
	c_ss = MMIntegerField('SS',max_value=59,min_value=0,null=True,blank=True) 
	c_ms = MMIntegerField('MS',max_value=999,min_value=0,null=True,blank=True) 

	arrival_station = models.ForeignKey('statistics.Station',
			null=True,blank=True,
		) 

	stations = models.ManyToManyField(Station,
			verbose_name="Related Stations",
			related_name='stations',
			null=True,blank=True,
			)

	classification = models.ForeignKey('Classification',
                        null=True,blank=True,
                )
 
	location = models.ForeignKey('Location',
                        null=True,blank=True,
                )

	
	frecuency = models.CharField(max_length=50,null=True,blank=True)
	located = models.BooleanField()
	latitude = models.FloatField(null=True,blank=True)
	longitude = models.FloatField(null=True,blank=True)
        deep = models.FloatField(null=True,blank=True)
	local_magnitude = models.FloatField(null=True,blank=True)
	duration_magnitude = models.FloatField(null=True,blank=True)
	surface_magnitude = models.FloatField(null=True,blank=True)
	
	checked = models.BooleanField()
	

	def __unicode__(self):
		return str('sismo.%s.%.2d%.2d'%(self.event_date.strftime('%Y%m%d'),
					self.p_hh,self.p_mm)
			  )


	class Meta:
		ordering = ['event_date']

import time
def handle_uploaded_file(f):
	for line in f.read().split('\n'):
		#print line.split(',')
		data = line.split(',')
		#[d,m,y] = data[0].split('. ')
		[d,m,y] = data[0].split(' ')

		from datetime import datetime
		event_date = datetime.strptime('%s %s %s'%(y,m,d), '%Y %m %d').date

		[p_hh,p_mm,ssms] = data[1].split(':')
		[p_ss,p_ms] = ssms.split('.')
		#flytia!
		p_hh = p_hh.split('"')[1]	
		p_ms = p_ms.split('"')[0]
			
		try:	
			[s_hh,s_mm,ssms2] = data[2].split(':')
			[s_ss,s_ms] = ssms2.split('.')
			#valres de la P
			s_hh = s_hh.split('"')[1]	
			s_ms = s_ms.split('"')[0]
			
		except:
			s_hh=0
			s_mm=0
			s_ss=0
			s_ms=0
		
		frec = data[3].split('"')[1]
		located = data[6]
		try:
			latitud = data[7].split('"')[1]
			longitud = data[8].split('"')[1]
		except:
			latitud = longitud = 0	
		try:
			deep = data[9].split('"')[1]
		except:
			deep = 0
		s = Seism(
			event_date='%s-%s-%s'%(y,m,d),
			p_hh=p_hh,
			p_mm=p_mm,
			p_ss=p_ss,
			p_ms=p_ms,
			s_hh=int(s_hh),
			s_mm=int(s_mm),
			s_ss=int(s_ss),
			s_ms=int(s_ms),
			frecuency=frec,
			located=located,
			latitude=latitud,
			longitude=longitud,
			deep=deep,
			#location_id=3 #Hudson
			location_id=2 #melimoyu
			)
		s.save()
		print s.event_date





