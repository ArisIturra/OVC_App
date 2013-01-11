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


		filename = 'map.ps'
		title = 'Hudson 26/11/2012'
		label = 'Longitud'
		try:
	
			try:
				f = open('tmp/seisms.sh', 'wr')
				f.write('#!/sbin/sh\n')
				
				f.write('ps=%s\n'%filename)
				f.write('gmtset GRID_PEN_PRIMARY thinnest,-\n')
				f.write('makecpt -Cseis -T0/50/10 > deep.cpt\n')
				f.write('makecpt -Ctopo -T0/2500/10 > g.cpt\n')
				

				f.write('grdimage w75s50.grd -R-73.5/-72.5/-46.2/-45.5 \\\n')
				f.write('-JM5i -E100 \\\n')
				f.write('-B0.25g0.25:."%s:" -Cg.cpt \\\n'%title)
				f.write('-X1i -Y5i \\\n')
				f.write('-P -K > $ps \n')
				
				f.write('psbasemap -R -J -O -K -Lf72:45:00W/46:08:00S/-45N/20k+u  >> $ps \n')
				f.write('psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps \n')
			
				for seism in q:
                        		if seism.located and seism.deep:
						f.write('%s %s %s %s \n'%(
							seism.longitude,
							seism.latitude,
							seism.deep,
							'0.1',#MAGNITUDE
							))
				f.write('END\n')

				
			
				f.write('psxy -R-73.5/-72.5/-50/2 \\\n')
				f.write('-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \\\n')
				f.write('-B0.25g0.25:"%s":/10g10:"Km":WS -O -K << END >> $ps \n'%label)
				
				for seism in q:
                        		if seism.located and seism.deep:
						f.write('%s %s %s %s \n'%(
							seism.longitude,
							seism.deep *-1,
							seism.deep,
							seism.deep,
							))
				f.write('END\n')

				f.write('psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \\\n')
				f.write('-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps \n')
				f.write('ps2pdf $ps\n')
				f.write('rm $ps deep.cpt g.cpt -f\n')

			finally:
		        	f.close()
		except IOError:
			pass

		f=open('tmp/seisms.sh', 'r')
		response = HttpResponse(f.read(),mimetype='application/x-sh')
		response['Content-Disposition'] = 'filename=seisms.sh'
		return response

	def seismName(self,obj):
		return str('%s.%.2d%.2d%.2d.%.3d'%(obj.event_date.strftime('%Y%m%d'),
                                        obj.p_hh,obj.p_mm,obj.p_ss,obj.p_ms)
                          )
	seismName.short_description = 'Id'


admin.site.register(Seism,SeismAdmin)
admin.site.register(Location)
admin.site.register(Classification)
