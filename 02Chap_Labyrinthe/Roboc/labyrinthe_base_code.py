# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""


class Labyrinthe:
    """Classe représentant un labyrinthe.
    Qui permet de conserver la position du robot, la grille de jeu, la derniere instruction du joueur et son nombre
    de répétition."""

    def __init__(self, map):
        self.robot_x = -1
        self.robot_y = -1
        self.robot_x_old = -1
        self.robot_x_old = -1
        self.grille_labyrinthe = map.labyrinthe
        self.grille_name = map.nom
        self.porte_passe = False
        self.rep_instruction = 1
        self.old_case_replace_by_robot = ' '
        self.instruction = 'A'
        print (self.grille_name)
        print (self.grille_labyrinthe)

        self.robot_x = recup_x_robot(self.grille_labyrinthe)
        self.robot_y = recup_y_robot(self.grille_labyrinthe)
        if self.robot_x == -1 or self.robot_y == -1:
            print("ERREUR LE PRGM N'A PAS TROUVE LA POSITION DU ROBOT (x, y)")
        #SUPPRIMER PRINT A LA FIN
        print ("1/ Dans la classe x = {}, y = {}".format(self.robot_x, self.robot_y))


def recup_x_robot(grille):
    """
    On recupère ici la la postion en colonne du robot, x commençant à 0
    :type grille: object
    """
    x = 0
    for ligne in grille:
        for case in ligne:
            if case == 'X':
                return x
            x += 1
        x = 0
    return -1


def recup_y_robot(grille):
    """ On récupère ici la postion en ligne du robot, y commençant par 0
    :type grille: object
    """
    y = 0
    for ligne in grille:
        for case in ligne:
            if case == 'X':
                return y
        y += 1
    return -1
