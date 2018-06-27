#!/usr/bin/python3.4
# -*-coding:Utf-8 -

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    
    def __init__(self, prenom): # Notre méthode constructeur
        """Constructeur de notre classe. Chaque attribut va être instancié
        avec une valeur par défaut... original""" 
        self.nom = "Dupont"
        self.prenom = prenom  # Quelle originalité
        self.age = 33 # Cela n'engage à rien
        self.lieu_residence = "Paris"

jean = Personne("Anthony")
print(jean.age)
print(jean.prenom)
print(Countet_nb_objects)
Paul = Personne("Paul")

