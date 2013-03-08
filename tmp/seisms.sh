#!/sbin/sh
ps=map.ps
cota=180
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2000/$cota > g.cpt
grdimage grid.grd -R-73.6962/-72.8678/-44.1252/-43.5848 \
-JM5i -E100 \
-B0.5g0.5:."2013/03/08:" -Cg.cpt \
-X1i -Y5i \
-P -K > $ps 
grdcontour grid.grd -R-73.6962/-72.8678/-44.1252/-43.5848 \
-JM5i -C$cota  -P -K  -O >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps 
-73.571 -43.672 16.1 0.1 
-73.48 -43.665 31.4 0.1 
-73.495 -43.662 32.9 0.1 
-73.451 -43.665 41.7 0.1 
-73.521 -43.668 34.3 0.1 
-72.945 -44.048 13.4 0.1 
-72.955 -44.046 13.7 0.1 
END
psxy -R-73.6962/-72.8678/-50/2 \
-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \
-B0.5g0.5:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-73.571 -16.1 16.1 16.1 
-73.48 -31.4 31.4 31.4 
-73.495 -32.9 32.9 32.9 
-73.451 -41.7 41.7 41.7 
-73.521 -34.3 34.3 34.3 
-72.945 -13.4 13.4 13.4 
-72.955 -13.7 13.7 13.7 
END
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \
-O -K -I0.3 -Ac -B500::/:m.s.n.m.:  >> $ps 
ps2pdf $ps
rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f
