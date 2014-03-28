#!/sbin/sh
ps=yanteles.ps
cota=180
grid=/opt/gmt/grid.grd
border=-74.082662/-72.225035/-43.953558/-43.139426
borderp=-74.082662/-72.225035
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2000/$cota > g.cpt
grdimage $grid -R$border \
-JM5i -E100 \
-B0.5g0.5:."Yanteles:" -Cg.cpt \
-X1i -Y7i \
-P -K > $ps
psbasemap -R -J -O -K -Lf73:30:00W/43:50:00S/-45N/40k+u  >> $ps
grdcontour $grid -R$border \
-JM5i -C$cota  -P -K  -O >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps
-73.507 -43.721 27.7 0.1 
-74.221 -43.347 26.0 0.1 
-73.551 -43.71 20.0 0.1 
-73.571 -43.672 16.1 0.1 
-73.566 -43.67 15.0 0.1 
END
psxy -R$borderp/-30/2 \
-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \
-B0.5g0.5:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-73.507 -27.7 27.7 27.7 
-74.221 -26.0 26.0 26.0 
-73.551 -20.0 20.0 20.0 
-73.571 -16.1 16.1 16.1 
-73.566 -15.0 15.0 15.0 
END
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \
-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps 
ps2pdf $ps 
rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f 
