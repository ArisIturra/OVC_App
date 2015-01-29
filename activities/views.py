# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import connection

from  seismicity.models import *

def index(request):
	quakes = Seism.objects.all().order_by('-id')[:10]
	print quakes
	return render_to_response('activity.html',locals())
