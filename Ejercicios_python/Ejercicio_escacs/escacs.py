# coding:utf-8
def my_range(inici, fi, increment):
	while inici <= fi:
		#Retorna l'element actual del rang (llista)
		yield inici
		inici = inici + increment
		
for fil in my_range (1,8,1):
	for col in my_range (1,8,1):
		if ((fil%2==0 and col%2==0)or(fil%2==1 and col%2==1)):
			print "#",
		else:
			print "@",
	print ""
