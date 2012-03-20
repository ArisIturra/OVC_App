from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

WAYCALL_CHOICES=(('Ph','phone'),('EM','E-Mail'),)
STATUS_CHOICE=((1,'open'),(2,'close'),)


class Logbook(models.Model):
    WayCall = models.CharField('Way Call requester',max_length=2,choices=WAYCALL_CHOICES)
    R_Mail = models.EmailField('E-Mail requester')
    R_Phone= PhoneNumberField('Phone requester')
    B_Date = models.DateField('Begin date ')
    B_Time = models.TimeField ('Begin time ')
    E_Date = models.DateField('End date ')
    E_Time = models.TimeField ('End time ')
    Requester = models.CharField(max_length=200)
    R_Status = models.CharField('Status',max_length=2,choices=STATUS_CHOICE, default=1)
    R_Solution= models.TextField('Requeste Solution')
         
    def was_published_today(self):
        return self.B_Date.date() == datetime.date.today()
    def __str__(self):
        return self.WayCall

class Status(models.Model):
    logbook = models.ForeignKey(Logbook)
    Solution = models.CharField(max_length=200)
    def __str__(self):
        return self.WayCall
