#!/usr/bin/python3.4
# -*-coding:Utf-8 

annee = input("Annee ...")
div = input("div ...")

try :
	annee = int(annee) / int(div)
except SyntaxError as exeption_ret: 
	print("Erreur de convertion de l'année", exeption_ret)
except TypeError :
	print("Hello")
except NameError :
	print("Hello bis")
except ZeroDivisionError as exeption_ret:
	print("La variable denominateur est égale à 0.", exeption_ret)
finally :
	print("END")
