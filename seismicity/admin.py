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
			'export_to_gmt_script',
			'export_to_3D_plot',
			'export_to_gmt_region',
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
	

	
		filename = 'region.ps'
		title = 'XI Regi\\363n'
		cota = '750'
		grid='/opt/gmt/grid.grd'
		border='-74.1890/-71.4070/-46.5465/-41.9463'
		borderp='-74.1890/-71.4070'
		

		locale=[]
                for seism in q:
                        if seism.located and seism.deep:
                                locale.append((seism.longitude, seism.latitude))
		
		try:
			try:
				f = open('tmp/region.sh', 'wr')
                                f.write('#!/sbin/sh\n')
				
				f.write('ps=%s\n'%filename)
                                f.write('cota=%s\n'%cota)
                                f.write('grid=%s\n'%grid)
				f.write('border=%s\n'%border)
				f.write('borderp=%s\n'%borderp)
	
	                        f.write('gmtset GRID_PEN_PRIMARY thinnest,-\n')
                                f.write('makecpt -Cseis -T0/50/10 > deep.cpt\n')
                                f.write('makecpt -Ctopo -T0/2000/$cota > g.cpt\n')
			
				f.write('grdimage $grid -R$border \\\n')
				f.write('-JM3.5i -E100 \\\n')
				f.write('-B0.5g0.5:."%s:" -Cg.cpt \\\n'%title)
				f.write('-Y2.6i \\\n')
				f.write('-P -K > $ps\n')

				f.write('grdcontour $grid -R$border \\\n')
				f.write('-JM3.5i -C$cota  -P -K  -O >> $ps \n')	
				f.write('psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps\n')
				                
		                for seism in q:
                                        if seism.located and seism.deep:
                                                f.write('%s %s %s %s \n'%(
                                                        seism.longitude,
                                                        seism.latitude,
                                                        seism.deep,
                                                        '0.1',#MAGNITUDE
                                                        ))
                                f.write('END\n')

				f.write('psxy -R$borderp/-50/2 \\\n')
				f.write('-JX3.5i/1.4i  -Wthick  -X0i -Y-1.8i -Cdeep.cpt  -Sc0.1i \\\n')
				f.write('-B0.5g0.5:"Longitud":/10g10:"Km":WS -O -K << END >> $ps \n')

		                for seism in q:
                                	if seism.located and seism.deep:
                                        	f.write('%s %s %s %s \n'%(
                                                        seism.longitude,
                                                        seism.deep *-1,
                                                        seism.deep,
                                                        seism.deep,
                                                        ))
                                f.write('END\n')


				f.write('psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y3.3i \\\n')
				f.write('-O -K -I0.3 -Ac -B500::/:m.s.n.m.:  >> $ps \n')
				f.write('ps2pdf $ps \n')
				f.write('rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f \n')

			finally:
                                f.close()
                except IOError:
                        pass

		f=open('tmp/region.sh', 'r')
                response = HttpResponse(f.read(),mimetype='application/x-sh')
                response['Content-Disposition'] = 'filename=region.sh'
                return response
		
	def export_to_gmt_script(self,request,q):

		
		filename = 'map.ps'
		title = date.today().strftime('%Y/%m/%d')
		label = 'Longitud'
		cota = '180' #TODO:TRANSLATE

		locale=[]
		for seism in q:
			if seism.located and seism.deep:
				locale.append((seism.longitude, seism.latitude))

		upper= map(max, zip(*locale))
		lower= map(min, zip(*locale))
				
		center = [((upper[0]+lower[0])/2),((upper[1]+lower[1])/2)]
		delta = [abs((lower[0]-upper[0])),abs((lower[1]-upper[1]))]


		contourn = [	(lower[0]-(delta[0]/5),upper[0]+(delta[1]/5)),
				(lower[1]-(delta[1]/5),upper[1]+(delta[1]/5))]
		try:
	
			try:
				f = open('tmp/seisms.sh', 'wr')
				f.write('#!/sbin/sh\n')
				
				f.write('ps=%s\n'%filename)
				f.write('cota=%s\n'%cota)
				f.write('gmtset GRID_PEN_PRIMARY thinnest,-\n')
				f.write('makecpt -Cseis -T0/50/10 > deep.cpt\n')
				f.write('makecpt -Ctopo -T0/2000/$cota > g.cpt\n')
				f.write('grdimage grid.grd -R%s/%s/%s/%s \\\n'%(
					contourn[0][0],contourn[0][1],
					contourn[1][0],contourn[1][1]
					))	
				f.write('-JM5i -E100 \\\n')
				f.write('-B%sg%s:."%s:" -Cg.cpt \\\n'%(0.5,0.5,title))
				f.write('-X1i -Y5i \\\n')
				f.write('-P -K > $ps \n')
				
	
				f.write('grdcontour grid.grd -R%s/%s/%s/%s \\\n'%(
					contourn[0][0],contourn[0][1],
					contourn[1][0],contourn[1][1]
					))	
				f.write('-JM5i -C$cota  -P -K  -O >> $ps \n')
				
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

				
			
				f.write('psxy -R%s/%s/-50/2 \\\n'%(
					contourn[0][0],contourn[0][1],
   					 ))
				f.write('-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \\\n')
				f.write('-B%sg%s:"%s":/%sg%s:"Km":WS -O -K << END >> $ps \n'%(
					0.5,0.5,label,
					10,10,
					))
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
				f.write('-O -K -I0.3 -Ac -B500::/:m.s.n.m.:  >> $ps \n')
				f.write('ps2pdf $ps\n')
				f.write('rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f\n')

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
