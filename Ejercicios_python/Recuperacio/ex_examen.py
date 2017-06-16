# !/usr/bin/python
# coding:utf-8
contador=0
def obtener_tamanyo(root,name):
	ruta_completa=os.path.join(root,name)
	tamanyo_archivo=os.stat(ruta_completa).st_size
	return tamanyo_archivo
	
def imprimir_total(contador):
	print "Se han borrado", contador ,"archivos"

import os
ruta_completa="/home/vlaguillo/test"
tamanyo_maximo=input('Pon el tamaño máximo: ')
 
for root, dir, files in os.walk(ruta_completa):
	for name in files:
		tamanyo_total=obtener_tamanyo(root,name)
		if (tamanyo_total <= tamanyo_maximo):
			comando="rm "+"-f "+os.path.join(root,name)
			os.system(comando)
			contador=contador+1
imprimir_total(contador)
