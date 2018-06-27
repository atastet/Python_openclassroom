#!/usr/bin/python3.4
# -*-coding:Utf-8 

class Tableau:
	"""Classe définissant une surface sur laquelle on peut écrire,
	que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
	est 'surface'"""	
	def __init__(self):
		self.surface = ""
	def ecrire(self, message_a_ecrire):
		if self.surface == "" : 
			self.surface += '\n'
		self.surface += message_a_ecrire
	def lire(self):
		print(self.surface)
	def effacer():
		self.surface=""
tab = Tableau()
print(tab.surface)
tab.ecrire("Hello world!")
tab.lire()
print(dir(tab))
