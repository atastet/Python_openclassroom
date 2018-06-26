#!/usr/bin/python3.4
# -*-coding:Utf-8

def fonction_inconnue(*en_liste, **en_dico):
	print("J'ai reçu : {} en param et {} en param nommés".format(en_liste, en_dico))

fonction_inconnue(1, 2, 3, Zizou = "Goal", Barthez = "Arret")
