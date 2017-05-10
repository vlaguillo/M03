def my_range(inici, fi, increment):
	while inici <= fi:
		#Retorna l'element actual del rang (llista)
		yield inici
		inici = inici + increment

for fil in my_range (1,4,1):
	for col in my_range (1,8,1):
		if (col==1 or col==8):
			print "*",
		else:
			if (fil==1 or fil==4):
				print "*",
			else:
				if (fil==2 and col==2):
					print "P",
				elif (fil==2 and col==3):
					print "Y",
				elif (fil==2 and col==4):
					print "T",
				elif (fil==2 and col==5): 
					print "H",
				elif (fil==2 and col==6): 
					print "O",
				elif (fil==2 and col==7): 
					print "N",
				else:
					print "-",
	print ""
