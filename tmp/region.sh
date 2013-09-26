#!/sbin/sh
ps=region.ps
cota=750
grid=/opt/gmt/grid.grd
border=-74.1890/-71.4070/-46.5465/-41.9463
borderp=-74.1890/-71.4070
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2000/$cota > g.cpt
grdimage $grid -R$border \
-JM3.5i -E100 \
-B0.5g0.5:."XI Regi\363n:" -Cg.cpt \
-Y2.6i \
-P -K > $ps
grdcontour $grid -R$border \
-JM3.5i -C$cota  -P -K  -O >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps
-73.73 -43.899 41.4 0.1 
-72.728 -44.094 14.0 0.1 
-72.723 -44.098 12.5 0.1 
-73.571 -43.672 16.1 0.1 
-73.008 -44.695 15.0 0.1 
-73.48 -43.665 31.4 0.1 
-73.495 -43.662 32.9 0.1 
-73.451 -43.665 41.7 0.1 
-73.521 -43.668 34.3 0.1 
-72.945 -44.048 13.4 0.1 
-72.955 -44.046 13.7 0.1 
-72.861 -44.045 12.1 0.1 
-74.292 -43.059 26.1 0.1 
-73.5 -43.663 30.9 0.1 
-73.566 -43.67 15.0 0.1 
-73.507 -43.721 27.7 0.1 
-73.551 -43.71 20.0 0.1 
END
psxy -R$borderp/-50/2 \
-JX3.5i/1.4i  -Wthick  -X0i -Y-1.8i -Cdeep.cpt  -Sc0.1i \
-B0.5g0.5:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-73.73 -41.4 41.4 41.4 
-72.728 -14.0 14.0 14.0 
-72.723 -12.5 12.5 12.5 
-73.571 -16.1 16.1 16.1 
-73.008 -15.0 15.0 15.0 
-73.48 -31.4 31.4 31.4 
-73.495 -32.9 32.9 32.9 
-73.451 -41.7 41.7 41.7 
-73.521 -34.3 34.3 34.3 
-72.945 -13.4 13.4 13.4 
-72.955 -13.7 13.7 13.7 
-72.861 -12.1 12.1 12.1 
-74.292 -26.1 26.1 26.1 
-73.5 -30.9 30.9 30.9 
-73.566 -15.0 15.0 15.0 
-73.507 -27.7 27.7 27.7 
-73.551 -20.0 20.0 20.0 
END
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y3.3i \
-O -K -I0.3 -Ac -B500::/:m.s.n.m.:  >> $ps 
ps2pdf $ps 
rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f 
