# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, map):
        self.robot_x = -1
        self.robot_y = -1
        self.grille_labyrinthe = map.labyrinthe
        self.grille_name = map.nom
        print (self.grille_name)
        print (self.grille_labyrinthe)
