import random
sortir=False
cartes=["1C","2C","3C","4C","5C","6C","7C","8C","9C","JC","QC","KC","AC","1D","2D","3D","4D","5D","6D","7D","8D","9D","JD","QD","KD","1P","2P","3P","4P","5P","6P","7P","8P","9P","JP","QP","KP","1T","2T","3T","4T","5T","6T","7T","8T","9T","JT","QT","KT"]
while (sortir==False):
	if (len(cartes) !=0):
		J1=(random.choice(cartes))
		cartes.remove(J1)
		print J1

	else:
		sortir=True
