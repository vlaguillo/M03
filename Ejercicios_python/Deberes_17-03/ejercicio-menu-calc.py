#coding: utf-8

import os

os.system('clear')
print "¿Que desea hacer el amo?"
print
print "S. Salir"
print "1. Sumar"
print "2. Restar"
print "3. Multiplicar"
print "4. Dividir"
print
opcion= raw_input("Introduzca una opción: ")


if opcion == "1":
		os.system('clear')
		print "Has selecionado la opción de sumar"
	
elif opcion == "2":
	os.system('clear')
	print "Has escogido la opción de restar"
	
	
elif opcion == "3":
	os.system('clear')
	print "Has escogido la opcion de multiplicar"
	
elif opcion == "4":
	os.system('clear')
	print "Has escogido la opción de dividir"
	
elif opcion == "S":
	os.system('clear')
	print "Has salido"
	
else:
	os.system('clear')
	print "Esa opción no existe" 
	
