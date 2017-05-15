# coding:utf8

#Defininim el my_range
def my_range(inici, fi, increment):
	while inici <= fi:
		#Retorna l'element actual del rang (llista)
		yield inici
		inici = inici + increment
		
#Importem el calendari		
import calendar

#Definim variables
cont=1			
mes=input('Pon el mes: ')
anyo=input('Pon el año: ')
monthRange = calendar.monthrange(anyo,mes)
#Al posar [1] vol dir que agafara el 2n parametre		
dias=monthRange[1]
#Al posar [0] vol dir que agafara el 1er parametre
dia_inicio=monthRange[0]
#La capçalera
print "L  M  X  J  V  S  D"
#En aquest bucle imprimira espais en blanc		
for col in my_range (1,dia_inicio-1,1):
	print "",
#Aquest tambe imprimira espais en blanc
for col in my_range (dia_inicio,7,1):
	print cont,
	cont=cont+1
#Imprimeix els dies
for fil in my_range (1,5,1):
	for col in my_range (1,7,1):
		if (cont<=dias):
			print cont,
		else:
			print "",
		cont=cont+1
	print ""
		
