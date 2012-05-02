from django.db import models
from django.forms import ModelForm
from django.contrib.localflavor.us.models import PhoneNumberField

WAYCALL_CHOICES=(('Ph','Phone'),('EM','Mail'),)
STATUS_CHOICE=(('1','open'),('2','close'),)

class Mail(models.Model):
	r_email = models.EmailField('E-Mail requester')

	def __unicode__(self):
		return u'%s'%(self.r_email)

class Phone(models.Model):
	r_phone= PhoneNumberField('Phone requester')

	def __unicode__(self):
		return u'%s'%(self.r_phone)
class Requester(models.Model):
	requester = models.CharField('Requester',max_length=200)

	def __unicode__(self):
		return u'%s'%(self.requester)



class Logbook(models.Model):
	mail = models.ForeignKey(Mail,blank=True,null=True)
	phone = models.ForeignKey(Phone,blank=True,null=True)
	b_request = models.DateTimeField('Begin request')
	e_request = models.DateTimeField('End request')
	requester = models.ForeignKey(Requester)
	request	= models.TextField('Request') 
	solution= models.TextField('Requeste Solution') 
   	status = models.CharField('Status',max_length=1,choices=STATUS_CHOICE, default=1)	

	def __unicode__(self):
		return u'%s %s'%(self.b_request,self.requester)


        def b_date(self):
                return self.b_request.date()
        def b_time(self):
                return self.b_request.time()

        def e_time(self):
                return self.e_request.time()

        def delta_time(self):
                return  self.e_request-self.b_request

	def export_sumary(modeladmin, request, queryset):
	        print queryset

        class Meta:
                ordering = ['b_request']
 
