#!/usr/bin/python3.4
# -*-coding:Utf-8

def	aff_float(fl) :
	if type(fl) is not float :
		raise TypeError("Le paramètre doit être un float")
	else : 
		vir = fl % 1
		fs = fl // 1
		
		
