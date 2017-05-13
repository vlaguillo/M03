#coding: utf-8

import os

os.system('clear')
#Indicamos al usuario las opciones
print "¿Que desea hacer el amo?"
print
print "S. Salir"
print "1. Sumar"
print "2. Restar"
print "3. Multiplicar"
print "4. Dividir"
print
opcion= raw_input("Introduzca una opción: ")

#Si opcion es 1
if opcion == "1":
		os.system('clear')
		print "Has selecionado la opción de sumar"

#Si opcion es 2	
elif opcion == "2":
	os.system('clear')
	print "Has escogido la opción de restar"
	
#Si opcion es 3	
elif opcion == "3":
	os.system('clear')
	print "Has escogido la opcion de multiplicar"

#Si opcion es 4	
elif opcion == "4":
	os.system('clear')
	print "Has escogido la opción de dividir"

#Si opcion es S	
elif opcion == "S":
	os.system('clear')
	print "Has salido"
	
else:
	os.system('clear')
	print "Esa opción no existe" 
