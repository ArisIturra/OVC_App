from django.forms import ModelForm
from django.contrib.admin import widgets
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from django.utils.safestring import mark_safe
from django.forms.formsets import formset_factory
from statistics.models import *
from django.contrib.admin.widgets import AdminDateWidget

class GetEvForm(forms.Form):
        stations = forms.ModelMultipleChoiceField(queryset=Station.objects.all(), 
                                                        widget=forms.CheckboxSelectMultiple()
                                                )

        start_date = forms.DateField(widget=AdminDateWidget())
        end_date = forms.DateField(widget=AdminDateWidget())


	def clean(self):
    		start_date = self.cleaned_data.get("start_date")
    		end_date = self.cleaned_data.get("end_date")
    		if end_date < start_date:
        		msg = u"End date should be greater than start date."
        		self._errors["end_date"] = self.error_class([msg])

