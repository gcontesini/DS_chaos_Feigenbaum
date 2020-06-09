reset

set xrange[5:8]

# pause -1

set terminal epslatex standalone color 12
set output "feigenbaum_diagram.tex"
plot "feigenbaum_diagram.txt" u 1:2 ps 0.1 lc black notitle


reset