#!/usr/bin/python3.4
# -*-coding:Utf-8 

from random import randrange
from math import ceil

def couleur(cagnotte, mise) :
	"""Fonction permettant de calculer le gain en cas de couleur ok"""
	cagnotte = ceil(cagnotte - mise + (mise * 1.5))
	print("Not bad x1.5")
	return (cagnotte)

try :
	cagnotte = input("Combien êtes vous prêt à jouer ... en $")
	int(cagnotte)
	assert cagnotte > 0 
	print("Ok commençons")
	while cagnotte > 0 :
		mise = input("Combien misez vous ?")
		int(mise)
		if mise <= 0 : 
			print("Pariez 0 ou un nombre négatif STOP le jeu")
			break
		if mise > cagnotte :
			print("Pas assez de money broo...")
			continue
		bet = input("Sur quel numéro ?")
		int(bet)
		if bet < 0 or bet > 49 :
			print("Pariez sur un nombre entre 0 et 49")
			continue
		result = randrange(50)
		print("Le croupiez a tire le ...")
		print(result)
		if result == bet :
			cagnotte = cagnotte - mise + (mise * 3)
			print ("Bingo x3")
		elif (bet  % 2 == 0) and (result % 2 == 0) :
			cagnotte = couleur(cagnotte, mise)
		elif (bet % 2 != 0 and result % 2 != 0) :
			cagnotte = couleur(cagnotte, mise)
		else :
			cagnotte = cagnotte - mise
			print("Dommage...")
		print("cagnotte =")
		print(cagnotte)
		result = 0
		stop = input("Souhaitez-vous quitter le casino oui => 1 si non => 0 ? ")
		int(stop)
		if stop == 1:
			print("Bye bye")
			break
		elif stop == 0 :
			continue
		else:
			print("Je n'ai pas compris votre reponse ... continuons")
	if cagnotte == 0 :
		print("Sorry you loose all your money")
	else : 
		print("Your money is :", cagnotte)
except AssertionError :
	print("Cagnotte doit être positive")
except NameError :
	print("Vous n'avez pas saisi de nombre")
except SyntaxError : 
	print("Saisissez un nombre correct")
