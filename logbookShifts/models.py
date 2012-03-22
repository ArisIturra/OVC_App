from django.db import models
from django.forms import ModelForm
from django.contrib.localflavor.us.models import PhoneNumberField

WAYCALL_CHOICES=(('Ph','Phone'),('EM','Mail'),)
STATUS_CHOICE=((1,'open'),(2,'close'),)

class Mail(models.Model):
	r_email = models.EmailField('E-Mail requester')

class Phone(models.Model):
	r_phone= PhoneNumberField('Phone requester')

class Requester(models.Model):
	requester = models.CharField('Requester',max_length=200)

class Logbook(models.Model):
#	WayCall = models.CharField('Way Call requester',max_length=2,choices=WAYCALL_CHOICES)
	mail = models.ForeignKey(Mail)
	phone = models.ForeignKey(Phone)
	b_request = models.DateTimeField('Begin request')
	e_request = models.DateTimeField('End request')
	requester = models.ForeignKey(Requester)
	r_solution= models.TextField('Requeste Solution') 
    
#	R_Status = models.CharField('Status',max_length=2,choices=STATUS_CHOICE, default=1)
###    
#    def was_published_today(self):
#        return self.B_Date.date() == datetime.date.today()

#    def __str__(self):
#        return self.WayCall



#

#








      
#class LogbookForm(ModelForm):
#    class Meta:
#        model = Logbook      
