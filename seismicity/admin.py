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
	list_filter = ['arrival_station','location','classification','checked']



	actions = [	'export_to_kml',
			'export_to_gmt_region',
			'export_to_gmt_corcovado',
			'export_to_gmt_fiordo',
			'export_to_gmt_hudson',
			'export_to_gmt_macacay',
			'export_to_gmt_melimoyu',
			'export_to_gmt_mentolat',
			'export_to_gmt_michimahuida',
			'export_to_gmt_yanteles',
			]

		
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



	def export_to_3D_plot(self,request,q):
	 

		filename = 'map.ps'
		title = 'Hudson 26/11/2012'
		label = 'Longitud'
		cota = '180' #TODO:TRANSLATE
		try:
	
			try:
				f = open('tmp/seisms.m', 'wr')
				f.write('\n')
				f.write('\n')
				f.write('\n')
				f.write('\n')
				f.write('\n')
	

				data =''
				for seism in q:
                        		if seism.located and seism.deep:
						data += '%s,%s,%s,"%s",'%(
							seism.longitude,
							seism.latitude,
							seism.deep,
							'o',
							)
				
				data= data[:-1]
				f.write('plot3(%s) \n'%data)
	

			finally:
		        	f.close()
		except IOError:
			pass
	def export_to_gmt_region(self,request,q):
		from gmtexport import gmtExport
                return gmtExport().region(q)
		
	def export_to_gmt_arenales(self,request,q):
		from gmtexport import gmtExport
                return gmtExport().arenales(q)

	def export_to_gmt_corcovado(self,request,q):
		from gmtexport import gmtExport
                return gmtExport().corcovado(q)
	
	def export_to_gmt_fiordo(self,request,q):
		from gmtexport import gmtExport
                return gmtExport().fiordo(q)
	
	def export_to_gmt_hudson(self,request,q):
		from gmtexport import gmtExport
                return gmtExport().hudson(q)

	def export_to_gmt_macacay(self,request,q):
		from gmtexport import gmtExport
                return gmtExport().macacay(q)
	
	def export_to_gmt_melimoyu(self,request,q):
		from gmtexport import gmtExport
                return gmtExport().melimoyu(q)

	def export_to_gmt_mentolat(self,request,q):
		from gmtexport import gmtExport
                return gmtExport().mentolat(q)

	def export_to_gmt_michimahuida(self,request,q):
		from gmtexport import gmtExport
                return gmtExport().michimahuida(q)

	def export_to_gmt_yanteles(self,request,q):
		from gmtexport import gmtExport
                return gmtExport().yanteles(q)

	
	def seismName(self,obj):
		return str('%s.%.2d%.2d%.2d.%.3d'%(obj.event_date.strftime('%Y%m%d'),
                                        obj.p_hh,obj.p_mm,obj.p_ss,obj.p_ms)
                          )
	seismName.short_description = 'Id'


admin.site.register(Seism,SeismAdmin)
admin.site.register(Location)
admin.site.register(Classification)
