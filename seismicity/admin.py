from seismicity.models import *
from statistics.models import *
from django.contrib import admin

from django.http import HttpResponse
import mimetypes
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _

class SeismAdminForm(forms.ModelForm):
	stations = forms.ModelMultipleChoiceField(
			queryset=Station.objects.all(), 
			required=False,
			widget=FilteredSelectMultiple(
				verbose_name='Stations',
				is_stacked=False
				)
			)
	class Meta:
		model = Seism

	def save(self, commit=True):
		seism = super(SeismAdminForm,self).save(commit=False)
		if commit:
			seism.save()

		if seism.pk:
			seism.stations = self.cleaned_data['stations']
			self.save_m2m()
		return seism
		
class SeismAdmin(admin.ModelAdmin):
	form = SeismAdminForm
	fieldsets = [
		(None, {'fields':[
				('event_date','checked'),
		                ('p_hh','p_mm','p_ss','p_ms'),
		                ('s_hh','s_mm','s_ss','s_ms'),
		                ('c_hh','c_mm','c_ss','c_ms'),
				('frecuency'),
				('stations','arrival_station'),
				('classification'),
				],
#			'classes': ('wide','extrapretty',),
			}
		),
		('Location', {'fields':[
				('latitude','longitude','deep'),
				('located','location')
				],
			}
		),
		('Data',{'fields':[
				('local_magnitude','duration_magnitude','surface_magnitude')
		]}
		)
	]
	date_hierarchy = 'event_date'

	list_display = ('seismName','arrival_station','latitude','longitude','deep','location','classification')
	list_filter = ['arrival_station','location','classification']



	actions = ['export_to_kml','export_to_gmt_script']


	def export_to_kml(self,request,q):
		
		import simplekml
		kml = simplekml.Kml()

		for seism in q:
			if seism.located and seism.deep:

				pnt = kml.newpoint(name='%s'%seism.deep)
				pnt.coords = [(seism.longitude,seism.latitude,float(seism.deep)*-1)]
				pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
				pnt.altitudemode = simplekml.AltitudeMode.clamptoground

		from datetime import datetime
		name = datetime.now().strftime('%Y%m%d-%H%M')+'.kml'

		
		response = HttpResponse(kml.kml(), mimetype='application/vnd.google-earth.kml+xml')
		response['Content-Disposition'] = 'filename=%s'%name

		return response

	def export_to_gmt_script(self,request,q):

		self.message_user(request,_('Not implemented yet'))


	def seismName(self,obj):
		return str('event at %s.%.2d%.2d%.2d'%(obj.event_date.strftime('%Y%m%d'),
                                        obj.p_hh,obj.p_mm,obj.p_ss)
                          )
	seismName.short_description = 'Id'


admin.site.register(Seism,SeismAdmin)
admin.site.register(Location)
admin.site.register(Classification)
