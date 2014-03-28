#!/sbin/sh
ps=melimoyu.ps
cota=250
grid=/opt/gmt/grid.grd
border=-73.868330/-72.050021/-44.559401/-43.772564
borderp=-73.868330/-72.050021
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2000/$cota > g.cpt
grdimage $grid -R$border \
-JM5i -E100 \
-B0.5g0.5:."Melimoyu:" -Cg.cpt \
-X1i -Y7i \
-P -K > $ps
psbasemap -R -J -O -K -Lf72:30:00W/44:28:00S/-45N/40k+u  >> $ps
grdcontour $grid -R$border \
-JM5i -C$cota  -P -K  -O >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps
-74.084 -44.487 16.4 0.1 
-72.728 -44.094 14.0 0.1 
-72.955 -44.046 13.7 0.1 
-72.945 -44.048 13.4 0.1 
-72.723 -44.098 12.5 0.1 
-72.861 -44.045 12.1 0.1 
END
psxy -R$borderp/-30/2 \
-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \
-B0.5g0.5:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-74.084 -16.4 16.4 16.4 
-72.728 -14.0 14.0 14.0 
-72.955 -13.7 13.7 13.7 
-72.945 -13.4 13.4 13.4 
-72.723 -12.5 12.5 12.5 
-72.861 -12.1 12.1 12.1 
END
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \
-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps 
ps2pdf $ps 
rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f 
