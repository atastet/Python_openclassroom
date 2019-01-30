# -*-coding:Utf-8 -*

from labyrinthe_base_code import Labyrinthe

"""Fonctions qui modifient la visualisation de la grille si le coup est jouable"""

def modif_grille(lab):
    """
    Fonction qui remplace par jeu de list et string les caractères qui doivent changer si le deplacement du robot
    a été accepté
    :param lab:
    :return:
    """
    new_string = list(lab.grille_labyrinthe[lab.robot_y_old])
    print(lab.grille_labyrinthe[lab.robot_y_old],lab.old_case_replace_by_robot)
    new_string[lab.robot_x_old] = lab.old_case_replace_by_robot
    print("OLD {}".format(new_string))
    lab.grille_labyrinthe[lab.robot_y_old] = "".join(new_string)
    print("lab gril y ={} {}".format(lab.robot_y_old,lab.grille_labyrinthe[lab.robot_y_old]))
    for ligne in lab.grille_labyrinthe:
        print("{}".format(ligne))
    new_string2 = list(lab.grille_labyrinthe[lab.robot_y])
    lab.old_case_replace_by_robot = new_string2[lab.robot_x]
    new_string2[lab.robot_x] = 'X'
    lab.grille_labyrinthe[lab.robot_y] = "".join(new_string2)
    #lab.old_case_replace_by_robot = lab.grille_labyrinthe[lab.robot_y][lab.robot_x]
    #lab.grille_labyrinthe[lab.robot_y][lab.robot_x] = 'X'
    print("____HELLLO____ \n: Je vais modifier la grille", lab)
    for ligne in lab.grille_labyrinthe:
        print("{}".format(ligne))