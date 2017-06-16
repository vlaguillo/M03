# coding:utf-8
import time
import os
sortir=True
sortir2=True
os.system('clear')
tabla=["Mesa","Ordenador","Altavoz","Silla"]
print tabla
time.sleep(1)
obj1=raw_input('Pon un objeto: ')
obj2=raw_input('Pon otro objeto: ')
tabla.append(obj1)
tabla.append(obj2)
time.sleep(1)
print tabla
time.sleep(1)
while (sortir==True):
	num=input('Que elemento quieres mostrar de la tabla (0 al 5): ')
	if (num > 5 or num < 0):
		print "No has puesto un numero válido"
	else:
		print tabla[num]
		sortir=False
while (sortir2==True):
	time.sleep(1)
	num2=input('Que elemento quieres eliminar (0 al 5): ')
	if (num2 > 5 or num < 0):
		print "No has puesto un numero válido"
	else:
		del tabla[num2]
		print tabla
		sortir2=False
