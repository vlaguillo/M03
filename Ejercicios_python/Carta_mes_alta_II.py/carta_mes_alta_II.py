# Coding: UTF-8
sortir=False
import os
from random import randint
os.system('clear')
while (sortir==False):
	J1n=randint(2,14)
	J1p=randint(1,4)
	J2n=randint(2,14)
	J2p=randint(1,4)

	numero1=J1n
	if (J1n==11):
		numero1="J"
	if (J1n==12):
		numero1="Q"
	if (J1n==13):
		numero1="K"
	if (J1n==14):
		numero1="A"

	if (J1p==1):
		pa="corazones"
	if (J1p==2):
		pa="trebols"
	if (J1p==3):
		pa="diamantes"
	if (J1p==4):
		pa="picas"
		
	numero2=J2n
	if (J2n==11):
		numero2="J"
	if (J2n==12):
		numero2="Q"
	if (J2n==13):
		numero2="K"
	if (J2n==14):
		numero2="A"

	if (J2p==1):
		pa="corazones"
	if (J2p==2):
		pa="treboles"
	if (J2p==3):
		pa="diamantes"
	if (J2p==4):
		pa="picas"

	print "J1:",numero1,"de",pa
	
	print "J2:",numero2,"de",pa

	if (J1n==J2n):
		print "Hay un empate"
	else:
		if (J1n>J2n):
			print "Gana el J1"
			sortir=True
		else:
			print "Gana J2"
			sortir=True
