#!/usr/bin/python3.4
# -*-coding:Utf-8 

class LigneInventaire:
	def __init__(self, produit, prix, quantite):
		self.produit = produit
		self.prix = prix
		self.quantite = quantite
	def __repr__(self):
		return "<Ligne d'inventaire {} ({}X{})>".format(self.produit, self.prix, self.quantite)

# Création de l'inventaire
inventaire = [
	LigneInventaire("pomme rouge", 1.2, 19),
	LigneInventaire("orange", 1.4, 24),
	LigneInventaire("banane", 0.9, 21),
	LigneInventaire("poire", 1.2, 24),
]

from operator import attrgetter
print(sorted(inventaire, key=attrgetter("prix", "quantite")))

inventaire.sort(key=attrgetter("quantite"), reverse=True)
print(sorted(inventaire, key=attrgetter("prix")))


