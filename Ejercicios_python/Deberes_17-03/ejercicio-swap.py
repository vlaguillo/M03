#coding: utf-8

import time

md = "movil"
mi = "bocadillo"

print "Las variables acutalmente:"
time.sleep(3)
print "Mano derecha",md
time.sleep(3)
print "Mano izquierda",mi
time.sleep(3)
print
print "Cambiando las variables de sitio"
time.sleep(3)
me = md
md = mi
mi = me
print
print "Mano derecha",md
time.sleep(3)
print "Mano izquierda",mi
time.sleep(3)
print
print "Cambio realizado con exito"
