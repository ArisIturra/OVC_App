#!/sbin/sh
ps=map.ps
cota=180
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2000/$cota > g.cpt
grdimage w75s50.grd -R-73.5/-72.5/-46.2/-45.5 \
-JM5i -E100 \
-B0.25g0.25:."Hudson 26/11/2012:" -Cg.cpt \
-X1i -Y5i \
-P -K > $ps 
grdcontour w75s50.grd -R-73.5/-72.5/-46.2/-45.5 \
-JM5i -C$cota  -P -K  -O >> $ps 
psbasemap -R -J -O -K -Lf72:45:00W/46:08:00S/-45N/20k+u  >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps 
-73.112 -45.916 15.0 0.1 
-73.078 -45.918 6.9 0.1 
-73.043 -46.0 13.4 0.1 
-73.0 -45.916 9.2 0.1 
-73.057 -45.916 7.2 0.1 
-73.021 -45.911 8.4 0.1 
-73.019 -45.921 8.5 0.1 
-73.106 -45.926 5.1 0.1 
END
psxy -R-73.5/-72.5/-50/2 \
-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \
-B0.25g0.25:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-73.112 -15.0 15.0 15.0 
-73.078 -6.9 6.9 6.9 
-73.043 -13.4 13.4 13.4 
-73.0 -9.2 9.2 9.2 
-73.057 -7.2 7.2 7.2 
-73.021 -8.4 8.4 8.4 
-73.019 -8.5 8.5 8.5 
-73.106 -5.1 5.1 5.1 
END
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \
-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps 
ps2pdf $ps
rm $ps deep.cpt g.cpt -f
