#!/usr/bin/python3.4
# -*-coding:Utf-8

class Zdict :
	"""Classe enveloppe d'un dictionnaire"""	
	def __init__(self):
		self._dictionnaire = {}
	def __getitem__(self, index):
		return self._dictionnaire[index]

	def __setitem__(self, index, value):
		"""Cette méthode est appelée quand on écrit objet[index] = valeur
        	On redirige vers self._dictionnaire[index] = valeur"""
		self._dictionnaire[index] = valeur
	def __contains__(self, valeur):
		if valeur in self._dictionnaire:
			return True
		else: 
			return False

Hello = Zdict
Hello[0] = 1
Hello[1] = 2
print(len(Hello))
