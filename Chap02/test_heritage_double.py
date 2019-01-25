#!/usr/bin/python3.4
# -*-coding:Utf-8

#class DoubleHer(Mere1, Mere2):
#	pass 

##Exeptions

class MonException(Exception):
	"""Exception levée dans un certain contexte… qui reste à définir"""
	def __init__(self, message):
		"""On se contente de stocker le message d'erreur"""
		self.message = message
	def __str__(self):
		"""On renvoie le message"""
		return self.message

raise MonException("Oups...j'ai tout casse")

