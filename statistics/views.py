# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

from statistics.models import *
#from manualData.forms import *
import statistics.charts

from django.shortcuts import render_to_response
from django.contrib import messages

from django.forms.models import modelformset_factory
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from django.template import RequestContext

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap
from django.conf import settings
from django import template

from time import gmtime, strftime

import datetime

class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))

def index(request):

	stations_list = Station.objects.all()


	gmap = maps.Map(opts = {
	#(up, left)
        'center': maps.LatLng(-44.7,-72),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 7.5,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
	        },
	    })

	for s in stations_list:
		marker = maps.Marker(opts = {
	        	'map': gmap,
       	 		'position': maps.LatLng(s.latitude,s.longitude),
    		})
		info = maps.InfoWindow({
	        	'content': 'Hello!',
        		'disableAutoPan': True
    		})
	    	info.open(gmap, marker)

#	context = {'form': MapForm(initial={'map': gmap})}
	from manualData.charts import Bars
	from manualData.reports import Report
	from manualData.maps import Cinematics

	b = Bars()
	r = Report()
	b_hist=b.get_histogram()
	
	#b_chart = b.get_bars(r.by_month('2010-11'))
	
	b_chart = b.get_bars(r.by_month())


	c =  Cinematics()
	
	cinematics = c.get_cinematics()		
	return render_to_response('index.html', locals() )



@csrf_exempt
def ev(request):
	
	stations_list = Station.objects.all()
	return render_to_response('ev.html',locals())



@csrf_exempt
def cinematics(request):
	from statistics.reports import Report
	
	r = Report()
	data = r.all()	
	try:
		year,month = strftime("%Y-%m", gmtime()).split('-')
	except:
		pass

	stations_list = Station.objects.all()
	for s in stations_list:
		p = data[s.name]
		evs = []
		evs1 = []
		evs2 = []
		evs3 = []
		for c in Choice.objects.all():
			evs1.append(len(Evaluation.objects.filter(
                                                        date__year=year,
                                                        date__month=month,
                                                        choice=c,
                                                        station=s
                                                        ))
				  )
			evs2.append(len(Evaluation.objects.filter(
                                                        date__year=year,
                                                        choice=c,
                                                        station=s
                                                        ))
				  )
			evs3.append(len(Evaluation.objects.filter(
                                                        choice=c,
                                                        station=s
                                                        ))
				  )
		evs.append(evs1)
		evs.append(evs2)
		evs.append(evs3)
		data[s.name] =  ([s.latitude,s.longitude],p,evs)
	
	
	gKey = settings.EASY_MAPS_GOOGLE_KEY
	return render_to_response('cinematics.html',locals())
	
@csrf_exempt
def update(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/admin')
	form = EvForm()
	if request.method == "POST":
		form = EvForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				messages.success(request, "Saved")
			except:
				messages.error(request, "Duplicate data.")
				
		else:
			messages.error(request, "Not Valid Form")
		
	return render_to_response('manualData/update.html',
			{
			'form':form,
			},
		context_instance=RequestContext(request)
	)



@csrf_exempt
def test(request):
	return render_to_response('manualData/test.html',
			{
#			'form':EvForm(),
			'formset':EvForm()
			},
			context_instance=RequestContext(request)
			)



def auto(request,data):

	try:	
		date = data[4:12]	
		hour = data[12:14]
		samples = int(data[14:])

		s = Station.objects.get(name=data[:4])

		percent = samples/3600

		if percent >= 98:
			c = Choice.objects.get(name='Verde')
		elif percent == 0:
			c = Choice.objects.get(name='Rojo')
		elif percent > 0 and percent < 50:
			c = Choice.objects.get(name='Naranjo')
		elif percent >= 50 and percent < 98:
			c = Choice.objects.get(name='Amarillo')
		else:
			c = Choice.objects.get(name='Rojo')

		e = Evaluation()

		e.station = s
		e.choice = c
		e.date = datetime.datetime.strptime(date,'%Y%m%d')
		e.hour = hour
		e.save()
		return HttpResponse('Ok')
	except ValueError as e:

		return HttpResponse(e)
