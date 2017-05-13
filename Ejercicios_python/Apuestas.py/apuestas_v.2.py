# -*-coding: utf-8-*-
import os
import time
from random import randint
#Iniciem les variables
dinero=100
sortir=False
os.system('clear')
while (sortir==False):
	time.sleep(1)
	os.system('clear')
	print "Tu saldo es de:",dinero
	apuesta=input("Pon tu apuesta, -1 para salir: ")
	#Fem les condicions
	if (dinero < 10):
		print "No puedes apostar mas"
		sortir=True
		
	if (apuesta > dinero):
		print "No tienes dinero suficiente"
			
	if (apuesta==-1):
		print "Adios"
		sortir=True
		
	if (apuesta < 10):
		print "La apuesta minima es de 10"
		sortir_apuesta=True	
		
	if (apuesta <= dinero and apuesta >= 10):
		dinero=dinero-apuesta
		print "Vamos a empezar"
		sortir_apuesta=False
		while (sortir_apuesta==False):
			#Tan el J1 com J2 agfaran cartes aleatories
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

			print "Banca:",numero1,"de",pa
			
			print "Tu:",numero2,"de",pa
			#En cas d'empat
			if (J1n==J2n):
				print "Hay un empate"
				dinero=dinero+apuesta
				sortir_apuesta=True
			else:
				#Perd el jugador
				if (J1n>J2n):
					print "Gana la banca"
					sortir_apuesta=True
					#No tens diners per jugar mes
					if (dinero < 10):
						print "No puedes apostar mas"
						sortir=True
						sortir_apuesta=True
				else:
					#Guanya J1
					print "Has ganado"
					dinero=dinero+(apuesta+apuesta)
					sortir_apuesta=True
					
					

