#!/usr/bin/python3.4
# -*-coding:Utf-8

def	aff_float(fl) :
	""" This function take a float in param and return a string with the troncature of this float with 3 decimal"""
	if type(fl) is not float :
		raise TypeError("Le paramètre doit être un float")
	else : 
		flottant = str(fl)
		entier, virgule  = flottant.split(".")
	return ",".join([entier, virgule[:3]])

