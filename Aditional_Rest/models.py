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

class RutUser(models.Model):
	"""User with app settings."""
	rut  = RutField(_('RUT'),unique= True,help_text='12.345.678-K')
    	user = models.ForeignKey(User, unique=True, related_name='profile')

	 # Use UserManager to get the create_user method, etc.
