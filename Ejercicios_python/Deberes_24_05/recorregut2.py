# coding: utf-8
import os
from os.path import join, getsize

pathToExplore = '/home/vlaguillo/M03'
#Mostrem NOMÉS els fitxers
for root,dirs,files in os.walk(pathToExplore):
	for name in dirs:
		name_path=os.path.join(name)
		print name_path
