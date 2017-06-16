# !/usr/bin/python
# coding:utf-8
import os, time
from time import gmtime, strftime

avui=strftime("%Y-%m-%d",gmtime())
ruta_a_explorar="/home/vlaguillo/M03"
total_size=0
 
for ruta, directorios, archivos in os.walk(ruta_a_explorar):
    for nombre in archivos:
        ruta_completa=os.path.join(ruta, nombre)
        print(ruta_completa)
 
        #Ultim cop accedit al fitxer
        print time.ctime(os.path.getatime(ruta_completa))
		#Mostrar data avui
        print avui
		#Mida dels fitxers
        total_size=total_size+os.stat(ruta_a_explorar).st_size
        print total_size
