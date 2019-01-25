# -*-coding:Utf-8

class People:  # def de la classe People
    """Classe People se def par les carateres suivant :
    - nom
    - prenom
    - age
    - lieu residence
     - taille """
    prenom = ...  # type: object
    _taille = ...  # type: float

    def __init__(self, nom, prenom):  # methode constructeur
        self.nom = nom
        self.prenom = prenom
        self.age = 23
        self.lieu_res = "Paris"
        self._taille = 1.81

    def __del__(self):
        """Supprime l'objet"""

        print("YOU KILLED HIM/HER")

    def __str__(self):
        """Affichage de l'objet quant on le print"""

        return """Je suis {}{}{}{}{}""".format(self.nom, self.prenom, self.age, self.lieu_res, self._taille)

    def grandir(self):
        """ Methode qui fait grandir de 10 cm"""

        self._taille += 0.02

    def petit(self):
        """Methode qui fait moins 5 cm"""

        self._taille -= 0.05

    def _set_taille(self, size):
        """Methode qui permet de renseigner la taille et supprime le 1.81 par default"""

        self._taille = size

    def _get_taille(self):
        """Imprime la taille"""

        print(self._taille)


Antho = People("Tastet", "Anthony")
print("""Je suis {0} {1} {2} ! Je vis a {3} Trop cool non ?""".format(Antho.nom, Antho.prenom, Antho._taille,
                                                                      Antho.lieu_res))
Antho.lieu_res = "Bayonne"
Antho._set_taille(1.70)
print("""Je suis {0} {1} {2} ! Je vis a {3} Trop cool non ?""".format(Antho.nom, Antho.prenom, Antho._taille,
                                                                      Antho.lieu_res))
Antho.grandir()
print("""Je suis {0} {1} {2} ! Je vis a {3} Trop cool non ?""".format(Antho.nom, Antho.prenom, Antho._taille,
                                                                      Antho.lieu_res))
Antho.petit()
print("""Je suis {0} {1} {2} ! Je vis a {3} Trop cool non ?""".format(Antho.nom, Antho.prenom, Antho._taille,
                                                                      Antho.lieu_res))
print(dir(People))
Antho._get_taille()
print(Antho)
Antho.__del__()
