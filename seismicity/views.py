from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from django import forms

from seismicity.models import handle_uploaded_file 
from seismicity.forms import UploadFileForm
@csrf_exempt

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
	        handle_uploaded_file(request.FILES['file'])
        	return HttpResponseRedirect('/upload_fileeer')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})
