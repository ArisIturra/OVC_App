# Create your views here.

from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response,RequestContext

from OVC_App.Aditional_Rest.models import *

@csrf_exempt
def details(request):
	
	ruser = Employee.objects.get(user=request.user)
	context =  {	'results': ruser.get_resolutions(),
		}
        return render_to_response('Aditional_Rest/recessrequest/details.html',
                 context_instance=RequestContext(request, context))
