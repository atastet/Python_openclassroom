#!/usr/bin/python3.4
# -*-coding:Utf-8 -

annee = input("Annee...")

try :
	annee = int(annee)
	assert annee > 0
except AssertionError : 
	print("Write positive year")
except TypeError:
    print("Vous n'avez pas saisi un nombre.")

