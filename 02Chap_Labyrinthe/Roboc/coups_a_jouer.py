# -*-coding:Utf-8 -*

from labyrinthe_base_code import Labyrinthe
from modif_grille_visu import *

""" Ces fonctions vont traiter tout ce qui a un rapport avec les coups à jouer:
    - Recuperer + Traiter les erreurs de frappe
    - Verifier la faisabilite
    - Jouer le coup
    """

def recup_coup_a_jouer(lab):
    """Recupere une instruction valable"""
    instruction_recup = raw_input("""Quel coup voulez vous jouer ? (ex : "E3" ou "N")\n""")
    lab.instruction  = instruction_recup[0].upper()
    while lab.instruction != 'N' and lab.instruction != 'E' and lab.instruction != 'S' and \
            lab.instruction != 'O' and lab.instruction != 'Q':
        instruction_recup = raw_input("""Ce coup ne fait pas partie de la gamme possible !
        Quel coup voulez vous jouer ? (ex : "E3" ou "N")\n""")
        lab.instruction  = instruction_recup[0].upper()
    instruction_recup = instruction_recup[1:]
    if instruction_recup != "":
        while True:
            try:
                instruction_recup = int(instruction_recup)
            except ValueError:
                print ("Vous devez rentrer une instruction valable cf. règles ci dessus ")
                instruction_recup = raw_input("""Quel coup voulez vous jouer ? (ex : "E3" ou "N")\n""")
                lab.instruction  = instruction_recup[0]
                instruction_recup = instruction_recup[1:]
                continue
            break
    else :
        instruction_recup = 1
    lab.rep_instruction = instruction_recup

def verif_case_libre(x, y, lab):
    """Fonction qui renvoie un int en fonction de la possibilité d'écrire ou non sur la case demandé"""

    if lab.grille_labyrinthe[y][x] == ' ' or lab.grille_labyrinthe[y][x] == 'X':
        return 0
    elif lab.grille_labyrinthe[y][x] == '.':
        return 1
    elif lab.grille_labyrinthe[y][x] == 'U':
        return 2
    elif lab.grille_labyrinthe[y][x] == 'O':
        return 3
    else :
        return -1

def enregistre_nouvelle_position(lab, x, y):
    """
    Fonction qui enregistre l'ancienne position du robot pour pouvoir l'effacer et enregistre les nouveaux x et y"
    :param lab:
    :param x:
    :param y:
    :return:
    """
    lab.robot_x_old = lab.robot_x
    lab.robot_y_old = lab.robot_y
    lab.robot_x = x
    lab.robot_y = y

def verif_coup_a_jouer(lab):
    """"Fonction qui verifie si le coup est jouable, si oui elle modifie les coordonnées de robot_x robot_y sauf si le jeu est gagné
    Cette fonction renvoie :
    100 si on demande une sauvegarde
    10 si le jeu est gagné
    -1 Si le coup est non-jouable
    0 Si la case est vide
    1 si c'est une porte"""

    x = lab.robot_x
    y = lab.robot_y
    ret = 0
    while lab.rep_instruction > 0:
        if lab.instruction == 'N':
            y += -1
        elif lab.instruction == 'S':
            y += 1
        elif lab.instruction == 'E':
            x += 1
        elif lab.instruction == 'O':
            x += -1
        elif lab.instruction == 'Q':
            ret = 100
            return ret
        ret = verif_case_libre(x,y,lab)
        if ret == 3 or ret == -1:
            return -1
        if ret == 2:
            return 10
        lab.rep_instruction -= 1
    enregistre_nouvelle_position(lab,x,y)
    return ret