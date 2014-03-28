#!/sbin/sh
ps=corcovado.ps
cota=400
grid=/opt/gmt/grid.grd
border=-73.870275/-72.021534/-43.649221/-42.839399
borderp=-73.870275/-72.021534
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2000/$cota > g.cpt
grdimage $grid -R$border \
-JM5i -E100 \
-B0.5g0.5:."Corcovado:" -Cg.cpt \
-X1i -Y7i \
-P -K > $ps
psbasemap -R -J -O -K -Lf72:20:00W/46:20:00S/-45N/100k+u  >> $ps
grdcontour $grid -R$border \
-JM5i -C$cota  -P -K  -O >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps
-74.292 -43.059 26.1 0.1 
-74.221 -43.347 26.0 0.1 
END
psxy -R$borderp/-30/2 \
-JX5i/1.4i  -Wthick  -X0i -Y-1.8i -Cdeep.cpt  -Sc0.1i \
-B0.5g0.5:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-74.292 -26.1 26.1 26.1 
-74.221 -26.0 26.0 26.0 
END
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \
-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps 
ps2pdf $ps 
rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f 
