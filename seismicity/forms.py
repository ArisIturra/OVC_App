from django.forms import ModelForm
from manualData.models import *
from django.contrib.admin import widgets
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from django.utils.safestring import mark_safe
from django.forms.formsets import formset_factory


class UploadFileForm(forms.Form):
    file  = forms.FileField()
