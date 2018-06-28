#!/usr/bin/python3.4
# -*-coding:Utf-8

class Personne : 

	""" Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""

	def __init__(self, nom, prenom):
		self.prenom = prenom
		self.nom = nom
		self.age = 33
		self._lieu_residence = "Paris" #par convention un _ permet d'indiquer qu'on y accede pas de l exter de la classe 

	def _get_lieu_de_residence(self):
		"""Méthode qui sera appelée quand on souhaitera accéder en lecture à l'attribut 'lieu_residence'"""
		print("On accede au lieu de residence")
		return self._lieu_residence
	
	def _set_lieu_de_residence(self, new_lieu):
		print("On modifie le lieu de residence de {} à {}".format(self._lieu_residence, new_lieu))
		self._lieu_residence = new_lieu

	lieu_residence = (_get_lieu_de_residence, _set_lieu_de_residence)

jean = Personne("Micado", "Jean")
print(jean.nom)
print(jean.lieu_residence)
jean.lieu_residence = "Berlin"
	
