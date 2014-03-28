#!/sbin/sh
ps=mentolat.ps
cota=180
grid=/opt/gmt/grid.grd
border=-73.806670/-72.431901/-45.049230/-44.464099
borderp=-73.806670/-72.431901
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2000/$cota > g.cpt
grdimage $grid -R$border \
-JM5i -E100 \
-B0.5g0.5:."Mentolat:" -Cg.cpt \
-X1i -Y7i \
-P -K > $ps
psbasemap -R -J -O -K -Lf72:45:00W/44:59:00S/-45N/40k+u  >> $ps
grdcontour $grid -R$border \
-JM5i -C$cota  -P -K  -O >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps
-74.084 -44.487 16.4 0.1 
-73.008 -44.695 15.0 0.1 
END
psxy -R$borderp/-30/2 \
-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \
-B0.5g0.5:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-74.084 -16.4 16.4 16.4 
-73.008 -15.0 15.0 15.0 
END
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \
-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps 
ps2pdf $ps 
rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f 
