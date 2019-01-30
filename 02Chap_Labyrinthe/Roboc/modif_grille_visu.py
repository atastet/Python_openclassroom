# -*-coding:Utf-8 -*

from labyrinthe_base_code import Labyrinthe

"""Fonctions qui modifient la visualisation de la grille si le coup est jouable"""

def modif_grille(lab):
    print(lab.grille_labyrinthe[lab.robot_y_old][lab.robot_x_old],lab.old_case_replace_by_robot)
    lab.grille_labyrinthe[lab.robot_y_old][lab.robot_x_old]= lab.old_case_replace_by_robot
    lab.old_case_replace_by_robot = lab.grille_labyrinthe[lab.robot_y][lab.robot_x]
    lab.grille_labyrinthe[lab.robot_y][lab.robot_x] = 'X'
    print("____HELLLO____ \n: Je vais modifier la grille", lab)
    for ligne in lab.grille_labyrinthe:
        print("{}\n".format(ligne))