# !/usr/bin/python
# coding:utf-8
import os
import stat

#Aixó sera on buscara els fitxers 
path_to_explore="/home/vlaguillo/M03"


for root, dirs, files in os.walk(path_to_explore):
    for name in files:
		#Posa la ruta + el nom del fitxer
        name_path=os.path.join(root, name)
        #Imprimeix per pantalla la ruta i el nom del fitxer
        print(name_path)
        permissions = stat.S_IMODE ( os.stat (name_path).st_mode )
        #Condició en la qual surten tots els fitxers que tenen algo diferent a 0 en others
        if (oct(permissions)[-1:])!=0:
			#Imprimeix els permisos
			print oct(permissions)
