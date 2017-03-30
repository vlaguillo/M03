#coding: utf-8
import os
os.system('clear')
import time
print "Escribe una de las 3 opciones para el J1:"
print "piedra"
print "papel"
print "tijeras"
J1 = raw_input("Pon una opción: ")
os.system('clear')
print "Escribe una de las 3 opciones para el J2:"
print "piedra"
print "papel"
print "tijeras"
J2 = raw_input ("Pon una opción: ")

if (J1 == "tijeras" and J2 == "piedra"):
	print "Gana J2"
	time.sleep(1)
	os.system('clear')
	
if (J1 == "tijeras" and J2 == "papel"):
	print "Gana J1"
	time.sleep(1)
	os.system('clear')
	
if (J1 == "piedra" and J2 == "tijeras"):
	print "Gana J1"
	time.sleep(1)
	os.system('clear')
	
if (J1 == "piedra" and J2 == "papel"):
	print "Gana J2"
	time.sleep(1)
	os.system('clear')
	
if (J1 == "papel" and J2 == "piedra"):
	print "Gana J1"
	time.sleep(1)
	os.system('clear')
	
if (J1 == "papel" and J2 == "tijeras"):
	print "Gana J2"
	time.sleep(1)
	os.system('clear')

if (J1 == J2):
	print "Empate"
	time.sleep(1)
	os.system('clear')
