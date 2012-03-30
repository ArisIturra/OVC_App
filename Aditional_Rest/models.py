from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.



from django.contrib.auth.models import User, UserManager
from django.contrib.localflavor.cl.forms import CLRutField


"""
Classification level that validates the chilean rut.
"""
class RutField(models.CharField):
	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = kwargs.get('max_length', 12)
		models.CharField.__init__(self, *args, **kwargs)

	def formfield(self, **kwargs):
		defaults = {'form_class': CLRutField}
		defaults.update(kwargs)
		return super(RutField, self).formfield(**defaults)

LEGAL_GRADE_CHOICES = (
		(0,_('Plant')), #TODO: Find tranlation!!
		(1,_('Contract')), 
		(2,_('Honorarium')), 
		)


HALF_DAY_CHOICES = (
		(0,_('AM')),
		(1,_('PM')),
		)
class RutUser(models.Model):
	"""User with app settings."""
	rut  = RutField(_('RUT'),unique= True,help_text=_('12.345.678-K'))
    	user = models.ForeignKey(User, unique=True, related_name='profile')
	grade = models.CharField(_('Grade'),max_length=50)	
	cost_center =  models.IntegerField(_('Cost Center'),)
	residence  = models.CharField(_('Recidence'),max_length=50)
	legal_grade = models.IntegerField(choices=LEGAL_GRADE_CHOICES)
	def __unicode__(self):
		return '%s'%self.user.username
	

	def get_available_days(self):

		acum = 0
		for res in  Recess.objects.filter(user=self):
			acum += res.available_days 	
		return acum

	def get_resolutions(self):

		return 	Recess.objects.filter(user=self)



class Recess(models.Model):
	"""Rest day wined"""

	user = models.ForeignKey(RutUser)
	resolution = models.CharField(_('Resolution number'),max_length=10)
	resolution_date = models.DateField(_('Resolution Date'))
	recess = models.FloatField(_('Recess days'),)
	available_days = models.FloatField(_('Available days'))

	from_date =  models.DateField(_('Resolution from date'), null=True,blank=True )
	to_date =  models.DateField(_('Resolution to date'), null=True,blank=True )
	resolution_days = models.FloatField(_('Days'), null=True,blank=True)

	
	def __unicode__(self):
		return "%s (%s)"%(self.resolution,self.user,)	



class RecessRequest(models.Model):
	"""Requet for a recess days"""

	requested_days = models.FloatField(_('Days'))
	user = models.ForeignKey(RutUser,editable=False)	
	halfday = models.IntegerField(choices=HALF_DAY_CHOICES,null=True,blank=True)
	begin  = models.DateField(_('Begin'))
	end  = models.DateField(_('End'))


	def __unicode__(self):
		return "%s [%s-%s] from %s"%(self.requested_days,self.begin,self.end,self.user)

