#!/sbin/sh
ps=map.ps
cota=180
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2000/$cota > g.cpt
grdimage grid.grd -R-73.1258/-73.042/-45.922/-45.915 \
-JM5i -E100 \
-B0.5g0.5:."2013/09/26:" -Cg.cpt \
-X1i -Y5i \
-P -K > $ps 
grdcontour grid.grd -R-73.1258/-73.042/-45.922/-45.915 \
-JM5i -C$cota  -P -K  -O >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps 
-73.112 -45.916 15.0 0.1 
-73.078 -45.918 6.9 0.1 
-73.043 -45.921 7.8 0.1 
END
psxy -R-73.1258/-73.042/-50/2 \
-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \
-B0.5g0.5:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-73.112 -15.0 15.0 15.0 
-73.078 -6.9 6.9 6.9 
-73.043 -7.8 7.8 7.8 
END
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \
-O -K -I0.3 -Ac -B500::/:m.s.n.m.:  >> $ps 
ps2pdf $ps
rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f
