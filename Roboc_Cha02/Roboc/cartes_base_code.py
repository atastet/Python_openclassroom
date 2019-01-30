# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

#On passe la carte d'un formart string en tableau

def creer_labyrinthe_depuis_chaine(chaine):
    """On passe la chaine en tableau pour obtenir une grille du type grid[y][x] pour pouvoir se situer en 2D
    :type chaine = str"""

    labyrinthe =[]
    line = ""
    for c in chaine:
        if c != '\r':
            if c != '\n':
                line += c
        else :
            labyrinthe.append(line)
            line =""
    labyrinthe.append(line)
    if labyrinthe[-1] == '':
        labyrinthe.__delitem__(-1)
    return labyrinthe

