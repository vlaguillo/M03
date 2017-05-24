import os
from os.path import join, getsize

pathToExplore = '/home/vlaguillo/M03'
#Mostrem les rutes mes l'arxiu
for root,dirs,files in os.walk(pathToExplore):
	for name in dirs:
		name_path=os.path.join(root, name)
		print name_path


