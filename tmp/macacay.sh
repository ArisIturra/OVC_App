#!/sbin/sh
ps=macacay.ps
cota=280
grid=/opt/gmt/grid.grd
border=-73.833530/-72.441113/-45.407302/-44.817388
borderp=-73.833530/-72.441113
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2000/$cota > g.cpt
grdimage $grid -R$border \
-JM5i -E100 \
-B0.5g0.5:."Maca-Cay:" -Cg.cpt \
-X1i -Y7i \
-P -K > $ps
psbasemap -R -J -O -K -Lf73:25:00W/45:20:00S/-45N/40k+u  >> $ps
grdcontour $grid -R$border \
-JM5i -C$cota  -P -K  -O >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps
-72.797 -45.386 19.1 0.1 
-72.873 -45.39 13.9 0.1 
-72.944 -45.366 10.6 0.1 
-72.925 -45.383 10.4 0.1 
-73.064 -45.372 10.2 0.1 
-73.087 -45.291 7.8 0.1 
-72.905 -45.201 0.1 0.1 
END
psxy -R$borderp/-30/2 \
-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \
-B0.5g0.5:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-72.797 -19.1 19.1 19.1 
-72.873 -13.9 13.9 13.9 
-72.944 -10.6 10.6 10.6 
-72.925 -10.4 10.4 10.4 
-73.064 -10.2 10.2 10.2 
-73.087 -7.8 7.8 7.8 
-72.905 -0.1 0.1 0.1 
END
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \
-O -K -I0.3 -Ac -B500::/:ms.n.m.:  >> $ps 
ps2pdf $ps 
rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f 
