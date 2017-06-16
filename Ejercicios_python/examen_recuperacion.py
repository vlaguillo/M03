# coding: utf-8
# !/usr/bin/python
import os
import time,os
cont_dir=0
cont_file=0
path_to_explore="./test"
print ""
for root,dirs,files in os.walk(path_to_explore):
	for name in dirs:
		ruta_completa=os.path.join(root,name)
		print "La ruta del directorio es:     ",ruta_completa
		cont_dir=cont_dir+1
	for name in files:
		ruta_completa=os.path.join(root,name)
		print "La ruta del fichero es:        ",ruta_completa
		tamanyo=os.stat(ruta_completa).st_size
		print "Su tamaño es de:               ",tamanyo,"B"
		cont_file=cont_file+1
		ult_mod=time.ctime(os.path.getmtime(ruta_completa))
		print "Su ultima modificación es del: ",ult_mod
print ""
print "Hay",cont_dir,"directorios y",cont_file,"ficheros"
print ""
