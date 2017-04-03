#coding: utf-8
sortir=False
num=31
TJ1=31
TJ2=31

while (sortir==False):

	if (TJ1%7==0 or TJ1%7==1):
		J1="tijeras"
	
	if (TJ1%7==2 or TJ1%7==3 or TJ1%7==6):
		J1="piedra"
	
	if (TJ1%7==4 or TJ1%7==5):
		J1="papel"
	
	if (TJ2%5==0 or TJ2%5==1):
		J2="papel"
	
	if (TJ2%5==2 or TJ2%5==3):
		J2="tijeras"
	
	if (TJ2%5==4):
		J2="piedra"
	
#---------------------------------------------

	if (J1 == "tijeras" and J2 == "piedra"):
		print "Gana J2"
	
	if (J1 == "tijeras" and J2 == "papel"):
		print "Gana J1"
	
	if (J1 == "piedra" and J2 == "tijeras"):
		print "Gana J1"
	
	if (J1 == "piedra" and J2 == "papel"):
		print "Gana J2"
	
	if (J1 == "papel" and J2 == "piedra"):
		print "Gana J1"
	
	if (J1 == "papel" and J2 == "tijeras"):
		print "Gana J2"

	if (J1 == J2):
		print "Empate"
	
	if (num==57):
		sortir=True
		
	num=num+1
	TJ1=TJ1+1
	TJ2=TJ2+1
