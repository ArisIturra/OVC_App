#!/sbin/sh
ps=hudson.ps
cota=250
grid=/opt/gmt/grid.grd
border=-73.715979/-72.267919/-46.210272/-45.613496
borderp=-73.715979/-72.267919
gmtset GRID_PEN_PRIMARY thinnest,-
makecpt -Cseis -T0/50/10 > deep.cpt
makecpt -Ctopo -T0/2000/$cota > g.cpt
grdimage $grid -R$border \
-JM5i -E100 \
-B0.5g0.5:."hudson:" -Cg.cpt \
-X1i -Y7i \
-P -K > $ps
grdcontour $grid -R$border \
-JM5i -C$cota  -P -K  -O >> $ps 
psxy -R -J -O -Cdeep.cpt  -Sci -Wthinnest -K << END >> $ps
-73.112 -45.916 15.0 0.1 
-73.078 -45.918 6.9 0.1 
-73.043 -45.921 7.8 0.1 
-73.056 -45.912 8.1 0.1 
-73.043 -45.904 13.4 0.1 
-73.02 -45.916 9.2 0.1 
-73.057 -45.916 7.2 0.1 
-73.021 -45.911 8.4 0.1 
-73.019 -45.921 8.5 0.1 
-73.106 -45.926 5.1 0.1 
-73.02 -45.934 11.0 0.1 
-73.017 -45.917 8.1 0.1 
-73.091 -45.969 9.7 0.1 
-73.097 -45.933 11.5 0.1 
-73.016 -45.942 11.5 0.1 
-73.051 -45.987 8.8 0.1 
-73.087 -45.935 7.8 0.1 
-73.029 -45.934 13.7 0.1 
-73.068 -45.958 10.9 0.1 
-73.085 -45.937 7.2 0.1 
-73.022 -45.93 8.7 0.1 
-73.079 -45.918 5.1 0.1 
-73.091 -45.958 8.2 0.1 
-73.022 -45.891 12.7 0.1 
-73.014 -45.892 11.6 0.1 
-73.069 -45.931 6.9 0.1 
-73.005 -45.88 8.3 0.1 
-73.026 -45.907 6.3 0.1 
-73.087 -45.291 7.8 0.1 
-73.058 -45.919 8.0 0.1 
-73.075 -45.876 25.8 0.1 
-73.072 -45.89 19.7 0.1 
-73.104 -45.906 15.0 0.1 
-72.983 -45.889 14.1 0.1 
-73.082 -45.892 19.0 0.1 
-73.071 -45.899 15.0 0.1 
-72.992 -45.975 15.0 0.1 
-73.039 -45.944 22.3 0.1 
-73.094 -45.886 26.5 0.1 
-73.062 -45.89 15.0 0.1 
-73.084 -45.894 10.0 0.1 
-73.003 -45.945 15.0 0.1 
-73.048 -45.903 8.0 0.1 
-73.095 -45.871 30.4 0.1 
-73.039 -45.961 7.4 0.1 
-73.095 -45.891 20.3 0.1 
-73.033 -45.901 6.3 0.1 
-73.063 -45.891 15.1 0.1 
-73.063 -45.891 15.1 0.1 
-73.078 -45.908 18.1 0.1 
-73.048 -45.901 20.8 0.1 
-73.064 -45.899 15.0 0.1 
-72.957 -45.89 16.7 0.1 
-73.009 -45.898 26.7 0.1 
-73.062 -45.892 15.0 0.1 
-73.04 -45.899 8.2 0.1 
-73.019 -45.962 12.0 0.1 
-72.978 -45.842 39.9 0.1 
-73.054 -45.899 8.0 0.1 
-72.95 -45.941 16.6 0.1 
-73.089 -45.899 9.7 0.1 
-73.012 -45.966 5.9 0.1 
-73.042 -45.876 15.0 0.1 
-72.969 -45.582 57.2 0.1 
-74.221 -43.347 26.0 0.1 
-72.905 -45.201 0.1 0.1 
-73.331 -42.3 0.3 0.1 
-73.064 -45.372 10.2 0.1 
-72.944 -45.366 10.6 0.1 
-72.925 -45.383 10.4 0.1 
-73.633 -44.49 46.4 0.1 
-72.873 -45.39 13.9 0.1 
-72.797 -45.386 19.1 0.1 
-77.37 -45.415 45.5 0.1 
-72.74 -43.816 42.4 0.1 
-74.084 -44.487 16.4 0.1 
-77.098 -45.967 42.5 0.1 
-77.004 -46.087 48.5 0.1 
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
-JX5i/1.4i  -Wthick  -X0i -Y-2.0i -Cdeep.cpt  -Sc0.1i \
-B0.5g0.5:"Longitud":/10g10:"Km":WS -O -K << END >> $ps 
-73.112 -15.0 15.0 15.0 
-73.078 -6.9 6.9 6.9 
-73.043 -7.8 7.8 7.8 
-73.056 -8.1 8.1 8.1 
-73.043 -13.4 13.4 13.4 
-73.02 -9.2 9.2 9.2 
-73.057 -7.2 7.2 7.2 
-73.021 -8.4 8.4 8.4 
-73.019 -8.5 8.5 8.5 
-73.106 -5.1 5.1 5.1 
-73.02 -11.0 11.0 11.0 
-73.017 -8.1 8.1 8.1 
-73.091 -9.7 9.7 9.7 
-73.097 -11.5 11.5 11.5 
-73.016 -11.5 11.5 11.5 
-73.051 -8.8 8.8 8.8 
-73.087 -7.8 7.8 7.8 
-73.029 -13.7 13.7 13.7 
-73.068 -10.9 10.9 10.9 
-73.085 -7.2 7.2 7.2 
-73.022 -8.7 8.7 8.7 
-73.079 -5.1 5.1 5.1 
-73.091 -8.2 8.2 8.2 
-73.022 -12.7 12.7 12.7 
-73.014 -11.6 11.6 11.6 
-73.069 -6.9 6.9 6.9 
-73.005 -8.3 8.3 8.3 
-73.026 -6.3 6.3 6.3 
-73.087 -7.8 7.8 7.8 
-73.058 -8.0 8.0 8.0 
-73.075 -25.8 25.8 25.8 
-73.072 -19.7 19.7 19.7 
-73.104 -15.0 15.0 15.0 
-72.983 -14.1 14.1 14.1 
-73.082 -19.0 19.0 19.0 
-73.071 -15.0 15.0 15.0 
-72.992 -15.0 15.0 15.0 
-73.039 -22.3 22.3 22.3 
-73.094 -26.5 26.5 26.5 
-73.062 -15.0 15.0 15.0 
-73.084 -10.0 10.0 10.0 
-73.003 -15.0 15.0 15.0 
-73.048 -8.0 8.0 8.0 
-73.095 -30.4 30.4 30.4 
-73.039 -7.4 7.4 7.4 
-73.095 -20.3 20.3 20.3 
-73.033 -6.3 6.3 6.3 
-73.063 -15.1 15.1 15.1 
-73.063 -15.1 15.1 15.1 
-73.078 -18.1 18.1 18.1 
-73.048 -20.8 20.8 20.8 
-73.064 -15.0 15.0 15.0 
-72.957 -16.7 16.7 16.7 
-73.009 -26.7 26.7 26.7 
-73.062 -15.0 15.0 15.0 
-73.04 -8.2 8.2 8.2 
-73.019 -12.0 12.0 12.0 
-72.978 -39.9 39.9 39.9 
-73.054 -8.0 8.0 8.0 
-72.95 -16.6 16.6 16.6 
-73.089 -9.7 9.7 9.7 
-73.012 -5.9 5.9 5.9 
-73.042 -15.0 15.0 15.0 
-72.969 -57.2 57.2 57.2 
-74.221 -26.0 26.0 26.0 
-72.905 -0.1 0.1 0.1 
-73.331 -0.3 0.3 0.3 
-73.064 -10.2 10.2 10.2 
-72.944 -10.6 10.6 10.6 
-72.925 -10.4 10.4 10.4 
-73.633 -46.4 46.4 46.4 
-72.873 -13.9 13.9 13.9 
-72.797 -19.1 19.1 19.1 
-77.37 -45.5 45.5 45.5 
-72.74 -42.4 42.4 42.4 
-74.084 -16.4 16.4 16.4 
-77.098 -42.5 42.5 42.5 
-77.004 -48.5 48.5 48.5 
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
psscale -Cg.cpt -D5.9i/2.5i/3i/0.35i -Y1.3i \
-O -K -I0.3 -Ac -B500::/:m.s.n.m.:  >> $ps 
ps2pdf $ps 
rm $ps deep.cpt g.cpt .gmtcommands4 .gmtdefaults4 -f 