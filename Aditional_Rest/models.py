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


STATUS_CHOICES = (
                (0,_('Wanting approval')),
                (1,_('Accepted')),
                (2,_('Rejected')),
                )

RECESS_STATUS_CHOICES = (
                (0,_('Available')),
                (1,_('Used')),
                (2,_('Transition')),
                )

HALF_DAY_CHOICES = (
		(0,_('AM')),
		(1,_('PM')),
		)

ACTIONS_CHOICES = (
		(0,_('Admin')),
		(1,_('User')),
		)

class RutUser(models.Model):
	"""User with app settings."""
	rut  = RutField(_('RUT'),unique= True,help_text=_('12.345.678-K'))
    	user = models.ForeignKey(User, unique=True, related_name='profile')

class Employee(RutUser):
	grade = models.CharField(_('Grade'),max_length=50)	
	cost_center =  models.IntegerField(_('Cost Center'),)
	residence  = models.CharField(_('Recidence'),max_length=50)
	legal_grade = models.IntegerField(choices=LEGAL_GRADE_CHOICES)
	recess_days = models.FloatField(_('Recess days'),null=True,blank=True,default=0,editable=False)
	accions = models.IntegerField(choices=ACTIONS_CHOICES,null=False,default=1)	


	def __unicode__(self):
		return '%s %s'%(self.user.username,self.rut)
	

	def get_resolutions(self):

		return 	Recess.objects.filter(user=self)



class Recess(models.Model):
	"""Rest day winned"""

	user = models.ForeignKey(Employee)
	resolution = models.CharField(_('Resolution number'),max_length=10)
	resolution_date = models.DateField(_('Resolution Date'))
	recess_days = models.FloatField(_('Recess days'),)
 	used_days = models.FloatField(_('Used days'),default=0,editable=False)
	status = models.IntegerField(choices=RECESS_STATUS_CHOICES,editable=False,default=0)

	from_date =  models.DateField(_('Resolution from date'), null=True,blank=True )
	to_date =  models.DateField(_('Resolution to date'), null=True,blank=True )
	resolution_days = models.FloatField(_('Days'), null=True,blank=True)


	

	def save(self,*args, **kwargs):
	
		if self.pk == None:	
			self.user.recess_days += self.recess_days
			self.user.save()	
		else:
			pass #TODO: Find the way to edit without alter recess_days



		super(Recess,self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s (%s)"%(self.resolution,self.user,)	

class RecessRequest(models.Model):
	"""Requet for a recess days"""

	requested_days = models.FloatField(_('Days'))
	user = models.ForeignKey(Employee,editable=False)	
	halfday = models.IntegerField(_('Halfday'),choices=HALF_DAY_CHOICES,null=True,blank=True)
	begin  = models.DateField(_('Begin'))
	end  = models.DateField(_('End'))
	status = models.IntegerField(choices=STATUS_CHOICES,editable=False,default=0)

	#def __unicode__(self):
	#	return "%s [%s-%s] from %s"%(self.requested_days,self.begin,self.end,self.user)
	
	def save(self,*args, **kwargs):
		"""Using save_model in admin.py """
		super(RecessRequest,self).save(*args, **kwargs)
