#!/usr/bin/python3.4
# -*-coding:Utf-8

import pickle

score = {"France" : 9, "Danemark" : 6, "Peru" : 3, "Australie" : 0}

with open('donnees', 'wb') as fichier:
	picky = pickle.Pickler(fichier)
	picky.dump(score)
# enregistrement
