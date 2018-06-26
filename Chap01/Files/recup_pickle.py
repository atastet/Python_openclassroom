#!/usr/bin/python3.4
# -*-coding:Utf-8

import pickle

with open("donnees", "rb") as fichier : 
	depicky = pickle.Unpickler(fichier)
	score = depicky.load()

print score
