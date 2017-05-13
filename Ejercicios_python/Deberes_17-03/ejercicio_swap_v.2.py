#coding: utf-8

import time

#Indicamos las variables
md = "movil"
mi = "bocadillo"

print "Las variables acutalmente:"
time.sleep(3)
print "Mano derecha",md
time.sleep(3)
print "Mano izquierda",mi
time.sleep(3)
print
#Cambiamos las variables
print "Cambiando las variables de sitio"
time.sleep(3)
me = md
md = mi
mi = me
print
#Resultado del cambio
print "Mano derecha",md
time.sleep(3)
print "Mano izquierda",mi
time.sleep(3)
print
print "Cambio realizado con exito"
