def my_range(inici, fi, increment):
	while inici <= fi:
		#Retorna l'element actual del rang (llista)
		yield inici
		inici = inici + increment
		
for fil in my_range(1,5,1):
	for col in my_range(1,4,1):
		if (fil==1 and col==2):
			print "A",
		elif (fil==1 and col==3):
			print "B",
		elif (fil==1 and col==4):
			print "C",
		elif (fil==2 and col==1):
			print "1",
		elif (fil==3 and col==1):
			print "2",
		elif (fil==4 and col==1):
			print "3",
		elif (fil==5 and col==1):
			print "4",
		elif (fil==3 and col==2):
			print "*",
		elif (fil==2 and col==3):
			print "*",
		else:
			print "-",
	print ""		
