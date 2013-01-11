#!/sbin/sh
ps=map.ps
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2500/10 > g.cpt
grdimage w75s50.grd -R-73.5/-72.5/-46.2/-45.5 \
-JM5i -E100 \
-B0.25g0.25:."Hudson 26/11/2012:" -Cg.cpt \
-X1i -Y5i \
-P -K > $ps 
psbasemap -R -J -O -K -Lf72:45:00W/46:08:00S/-45N/20k+u  >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps 
-73.112 -45.916 15.0 0.1 
-73.078 -45.918 6.9 0.1 
-73.043 -45.921 7.8 0.1 
-73.056 -45.912 8.1 0.1 
-73.043 -46.0 13.4 0.1 
END
psxy -R-73.5/-72.5/-50/2 \
-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \
-B0.25g0.25:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-73.112 -15.0 15.0 15.0 
-73.078 -6.9 6.9 6.9 
-73.043 -7.8 7.8 7.8 
-73.056 -8.1 8.1 8.1 
-73.043 -13.4 13.4 13.4 
END
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \
-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps 
ps2pdf $ps
rm $ps deep.cpt g.cpt -f
