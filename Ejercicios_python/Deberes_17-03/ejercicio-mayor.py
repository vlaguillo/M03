#coding: utf-8

num1 = input("Indique el primer numero: ")
num2 = input("Indique el segundo numero: ")

if (num1 < num2):
	print num1,"es mas pequeño que",num2
	
else:
	if (num1 > num2):
		print num1,"es mas grande que",num2
	
	else:
		print num1,"y",num2,"son iguales"
