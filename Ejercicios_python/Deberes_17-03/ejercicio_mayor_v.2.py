#coding: utf-8

#El usuario establecera las variables
num1 = input("Indique el primer numero: ")
num2 = input("Indique el segundo numero: ")

#num1 es mas pequeño que num2
if (num1 < num2):
	print num1,"es mas pequeño que",num2
	
else:
	#Si num1 es mas grande que num2
	if (num1 > num2):
		print num1,"es mas grande que",num2
	
	else:
		#Si son iguales
		print num1,"y",num2,"son iguales"
