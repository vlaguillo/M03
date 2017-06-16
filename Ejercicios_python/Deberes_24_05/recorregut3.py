import os
from os.path import join, getsize

pathToExplore = '/home/vlaguillo/M03'
#Mostrem els fitxers amb la ruta i el que ocupa cada un
for root,dirs,files in os.walk(pathToExplore):
	for name in files:
		name_path=os.path.join(root, name)
		print name_path
		print os.path.getsize(name_path)
