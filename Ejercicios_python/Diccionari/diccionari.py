# coding:utf-8
print "Els meus Vocaloids preferits:"
diccionari={'1':'Akita Neru', '2':'Hatsune Miku', '3':'Kagamine Len', '4':'Megpoid Gumi', '5':'Kasane Teto', '6':'Meiko'}
opcio=raw_input('Posa un numero del 1 al 6: ')
print diccionari[opcio]
print ""

print "Ara afegeix tu algo"
texto=raw_input('Afexeix el que vulguis que es mostri: ')
clave=input('Posa un numero que sera la clau: ')
diccionari[clave]=texto
print "imprimint nou diccionari"
print diccionari
print ""
print "Ensenyant la nova entrada"
print diccionari[clave]

