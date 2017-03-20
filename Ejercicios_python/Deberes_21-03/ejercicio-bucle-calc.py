#coding: utf-8

import os
import time

salir = False

while (salir==False):
	print "S. Salir"
	print "1. Sumar"
	print "2. Restar"
	print "3. Dividir"
	print "4. Multiplicar"
	print 
	print ("¿Que desa hacer el amo?")
	tecla=raw_input("Pon una opcion: ")
	if (tecla=="1"):
		os.system('clear')
		print "Has escogido la opcion de sumar"
		time.sleep(2)
		os.system('clear')
		
	elif (tecla=="2"):
		os.system('clear')
		print "Has escogido la opcion de restar"
		time.sleep(2)
		os.system('clear')
		
	elif (tecla=="3"):
		os.system('clear')
		print "Has escogido la opcion de dividir"
		time.sleep(2)
		os.system('clear')
		
	elif (tecla=="4"):
		os.system('clear')
		print "Has escogido la opcion de multiplicar"
		time.sleep(2)
		os.system('clear')
		
	elif (tecla=="S"):
		os.system('clear')
		print "Adios"
		salir=True
		
	else:
		os.system('clear')
		print "La opción que has puesto es erronea"
		time.sleep(2)
		os.system('clear')
 
