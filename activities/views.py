# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import connection

from  seismicity.models import *

from django import template


def index(request):
	quakes = Seism.objects.all().order_by('-id')[:10]
	return render_to_response('activity.html',locals())

