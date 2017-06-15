# !/usr/bin/python
# coding:utf-8
import os
import stat
 
path_to_explore="./test"
        
# Mostrem ruta tot    
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        ruta_completa=os.path.join(root, name)
        os.chmod(ruta_completa,0660)
        print(ruta_completa) ,
        permissions = stat.S_IMODE (os.stat (ruta_completa).st_mode)
        print oct(permissions)
