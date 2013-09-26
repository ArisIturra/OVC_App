#TODO: POO plz use Ur brain!!!!!
#Did you hear about encapsulation?

from django.http import HttpResponse
class gmtExport():

	def region(self,q):
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
                        	f.write('-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps \n')
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



	def corcovado(self,q):
		filename = 'corcovado.ps'
	       	title = 'Corcovado'
	        cota = '400'
	        grid='/opt/gmt/grid.grd'
	        border='-73.870275/-72.021534/-43.649221/-42.839399'
	        borderp='-73.870275/-72.021534'


	        locale=[]
       		for seism in q:
        		if seism.located and seism.deep:
                		locale.append((seism.longitude, seism.latitude))

		try:
	        	try:
	                	f = open('tmp/corcovado.sh', 'wr')
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
                        	f.write('-JM5i -E100 \\\n')
                        	f.write('-B0.5g0.5:."%s:" -Cg.cpt \\\n'%title)
                        	f.write('-X1i -Y7i \\\n')
                        	f.write('-P -K > $ps\n')

                        	f.write('grdcontour $grid -R$border \\\n')
                        	f.write('-JM5i -C$cota  -P -K  -O >> $ps \n')
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
                        	f.write('-JX5i/1.4i  -Wthick  -X0i -Y-1.8i -Cdeep.cpt  -Sc0.1i \\\n')
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


                      	 	f.write('psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \\\n')
                        	f.write('-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps \n')
                        	f.write('ps2pdf $ps \n')
                        	f.write('rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f \n')

             	 	finally:
                		f.close()
		except IOError:
        		pass

		f=open('tmp/corcovado.sh', 'r')
        	response = HttpResponse(f.read(),mimetype='application/x-sh')
       		response['Content-Disposition'] = 'filename=corcovado.sh'
        	return response




	def fiordo(self,q):
		filename = 'fiordo.ps'
	       	title = 'Fiordo Ays\\351n'
	        cota = '280'
	        grid='/opt/gmt/grid.grd'
	        border='-73.391813/-72.004071/-45.709353/-45.125016'
	        borderp='-73.391813/-72.004071'


	        locale=[]
       		for seism in q:
        		if seism.located and seism.deep:
                		locale.append((seism.longitude, seism.latitude))

		try:
	        	try:
	                	f = open('tmp/fiordo.sh', 'wr')
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
                        	f.write('-JM5i -E100 \\\n')
                        	f.write('-B0.5g0.5:."%s:" -Cg.cpt \\\n'%title)
                        	f.write('-X1i -Y7i \\\n')
                        	f.write('-P -K > $ps\n')

                        	f.write('grdcontour $grid -R$border \\\n')
                        	f.write('-JM5i -C$cota  -P -K  -O >> $ps \n')
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
                        	f.write('-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \\\n')
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


                      	 	f.write('psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \\\n')
                        	f.write('-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps \n')
                        	f.write('ps2pdf $ps \n')
                        	f.write('rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f \n')

             	 	finally:
                		f.close()
		except IOError:
        		pass

		f=open('tmp/fiordo.sh', 'r')
        	response = HttpResponse(f.read(),mimetype='application/x-sh')
       		response['Content-Disposition'] = 'filename=fiordo.sh'
        	return response


	def hudson(self,q):
		filename = 'hudson.ps'
	       	title = 'hudson'
	        cota = '250'
	        grid='/opt/gmt/grid.grd'
	        border='-73.715979/-72.267919/-46.210272/-45.613496'
	        borderp='-73.715979/-72.267919'


	        locale=[]
       		for seism in q:
        		if seism.located and seism.deep:
                		locale.append((seism.longitude, seism.latitude))

		try:
	        	try:
	                	f = open('tmp/hudson.sh', 'wr')
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
                        	f.write('-JM5i -E100 \\\n')
                        	f.write('-B0.5g0.5:."%s:" -Cg.cpt \\\n'%title)
                        	f.write('-X1i -Y7i \\\n')
                        	f.write('-P -K > $ps\n')

                        	f.write('grdcontour $grid -R$border \\\n')
                        	f.write('-JM5i -C$cota  -P -K  -O >> $ps \n')
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
                        	f.write('-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \\\n')
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


                      	 	f.write('psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \\\n')
                        	f.write('-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps \n')
                        	f.write('ps2pdf $ps \n')
                        	f.write('rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f \n')

             	 	finally:
                		f.close()
		except IOError:
        		pass

		f=open('tmp/hudson.sh', 'r')
        	response = HttpResponse(f.read(),mimetype='application/x-sh')
       		response['Content-Disposition'] = 'filename=hudson.sh'
        	return response

	def macacay(self,q):
		filename = 'macacay.ps'
	       	title = 'Maca-Cay'
	        cota = '280'
	        grid='/opt/gmt/grid.grd'
	        border='-73.833530/-72.441113/-45.407302/-44.817388'
	        borderp='-73.833530/-72.441113'


	        locale=[]
       		for seism in q:
        		if seism.located and seism.deep:
                		locale.append((seism.longitude, seism.latitude))

		try:
	        	try:
	                	f = open('tmp/macacay.sh', 'wr')
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
                        	f.write('-JM5i -E100 \\\n')
                        	f.write('-B0.5g0.5:."%s:" -Cg.cpt \\\n'%title)
                        	f.write('-X1i -Y7i \\\n')
                        	f.write('-P -K > $ps\n')

                        	f.write('grdcontour $grid -R$border \\\n')
                        	f.write('-JM5i -C$cota  -P -K  -O >> $ps \n')
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
                        	f.write('-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \\\n')
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


                      	 	f.write('psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \\\n')
                        	f.write('-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps \n')
                        	f.write('ps2pdf $ps \n')
                        	f.write('rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f \n')

             	 	finally:
                		f.close()
		except IOError:
        		pass

		f=open('tmp/macacay.sh', 'r')
        	response = HttpResponse(f.read(),mimetype='application/x-sh')
       		response['Content-Disposition'] = 'filename=macacay.sh'
        	return response

	def melimoyu(self,q):
		filename = 'melimoyu.ps'
	       	title = 'Melimoyu'
	        cota = '250'
	        grid='/opt/gmt/grid.grd'
	        border='-73.868330/-72.050021/-44.559401/-43.772564'
	        borderp='-73.868330/-72.050021'


	        locale=[]
       		for seism in q:
        		if seism.located and seism.deep:
                		locale.append((seism.longitude, seism.latitude))

		try:
	        	try:
	                	f = open('tmp/melimoyu.sh', 'wr')
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
                        	f.write('-JM5i -E100 \\\n')
                        	f.write('-B0.5g0.5:."%s:" -Cg.cpt \\\n'%title)
                        	f.write('-X1i -Y7i \\\n')
                        	f.write('-P -K > $ps\n')

                        	f.write('grdcontour $grid -R$border \\\n')
                        	f.write('-JM5i -C$cota  -P -K  -O >> $ps \n')
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
                        	f.write('-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \\\n')
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


                      	 	f.write('psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \\\n')
                        	f.write('-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps \n')
                        	f.write('ps2pdf $ps \n')
                        	f.write('rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f \n')

             	 	finally:
                		f.close()
		except IOError:
        		pass

		f=open('tmp/melimoyu.sh', 'r')
        	response = HttpResponse(f.read(),mimetype='application/x-sh')
       		response['Content-Disposition'] = 'filename=melimoyu.sh'
        	return response

	def mentolat(self,q):
		filename = 'mentolat.ps'
	       	title = 'Mentolat'
	        cota = '180'
	        grid='/opt/gmt/grid.grd'
	        border='-73.806670/-72.431901/-45.049230/-44.464099'
	        borderp='-73.806670/-72.431901'


	        locale=[]
       		for seism in q:
        		if seism.located and seism.deep:
                		locale.append((seism.longitude, seism.latitude))

		try:
	        	try:
	                	f = open('tmp/mentolat.sh', 'wr')
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
                        	f.write('-JM5i -E100 \\\n')
                        	f.write('-B0.5g0.5:."%s:" -Cg.cpt \\\n'%title)
                        	f.write('-X1i -Y7i \\\n')
                        	f.write('-P -K > $ps\n')

                        	f.write('grdcontour $grid -R$border \\\n')
                        	f.write('-JM5i -C$cota  -P -K  -O >> $ps \n')
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
                        	f.write('-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \\\n')
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


                      	 	f.write('psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \\\n')
                        	f.write('-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps \n')
                        	f.write('ps2pdf $ps \n')
                        	f.write('rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f \n')

             	 	finally:
                		f.close()
		except IOError:
        		pass

		f=open('tmp/mentolat.sh', 'r')
        	response = HttpResponse(f.read(),mimetype='application/x-sh')
       		response['Content-Disposition'] = 'filename=mentolat.sh'
        	return response

	def michimahuida(self,q):
		filename = 'michimahuida.ps'
	       	title = 'Michimahuida'
	        cota = '180'
	        grid='/opt/gmt/grid.grd'
	        border='-73.329043/-71.852779/-43.242040/-42.588446'
	        borderp='-73.329043/-71.852779'


	        locale=[]
       		for seism in q:
        		if seism.located and seism.deep:
                		locale.append((seism.longitude, seism.latitude))

		try:
	        	try:
	                	f = open('tmp/michimahuida.sh', 'wr')
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
                        	f.write('-JM5i -E100 \\\n')
                        	f.write('-B0.5g0.5:."%s:" -Cg.cpt \\\n'%title)
                        	f.write('-X1i -Y7i \\\n')
                        	f.write('-P -K > $ps\n')

                        	f.write('grdcontour $grid -R$border \\\n')
                        	f.write('-JM5i -C$cota  -P -K  -O >> $ps \n')
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
                        	f.write('-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \\\n')
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


                      	 	f.write('psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \\\n')
                        	f.write('-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps \n')
                        	f.write('ps2pdf $ps \n')
                        	f.write('rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f \n')

             	 	finally:
                		f.close()
		except IOError:
        		pass

		f=open('tmp/michimahuida.sh', 'r')
        	response = HttpResponse(f.read(),mimetype='application/x-sh')
       		response['Content-Disposition'] = 'filename=michimahuida.sh'
        	return response
	


	def yanteles(self,q):
		filename = 'yanteles.ps'
	       	title = 'Yanteles'
	        cota = '180'
	        grid='/opt/gmt/grid.grd'
	        border='-74.082662/-72.225035/-43.953558/-43.139426'
	        borderp='-74.082662/-72.225035'


	        locale=[]
       		for seism in q:
        		if seism.located and seism.deep:
                		locale.append((seism.longitude, seism.latitude))

		try:
	        	try:
	                	f = open('tmp/yanteles.sh', 'wr')
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
                        	f.write('-JM5i -E100 \\\n')
                        	f.write('-B0.5g0.5:."%s:" -Cg.cpt \\\n'%title)
                        	f.write('-X1i -Y7i \\\n')
                        	f.write('-P -K > $ps\n')

                        	f.write('grdcontour $grid -R$border \\\n')
                        	f.write('-JM5i -C$cota  -P -K  -O >> $ps \n')
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
                        	f.write('-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \\\n')
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


                      	 	f.write('psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \\\n')
                        	f.write('-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps \n')
                        	f.write('ps2pdf $ps \n')
                        	f.write('rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f \n')

             	 	finally:
                		f.close()
		except IOError:
        		pass

		f=open('tmp/yanteles.sh', 'r')
        	response = HttpResponse(f.read(),mimetype='application/x-sh')
       		response['Content-Disposition'] = 'filename=yanteles.sh'
        	return response

