# !/usr/bin/python
# coding:utf-8
import os
 
path_to_explore=raw_input('Posa la ruta: ')
 
 
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        ruta_completa=os.path.join(root, name)
        print(ruta_completa)
