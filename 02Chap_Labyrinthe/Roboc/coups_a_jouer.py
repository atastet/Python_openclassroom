# -*-coding:Utf-8 -*

from labyrinthe_base_code import Labyrinthe

""" Ces fonctions vont traiter tout ce qui a un rapport avec les coups à jouer:
    - Recuperer + Traiter les erreurs de frappe
    - Verifier la faisabilite
    - Jouer le coup
    """

def recup_coup_a_jouer(lab):
    """Recupere une instruction valable"""
    instruction_recup = input("""Quel coup voulez vous jouer ? (ex : "E3" ou "N")\n...""")
    lab.instruction  = instruction_recup[0]
    while lab.instruction != 'N' and lab.instruction != 'E' and lab.instruction != 'S' and \
            lab.instruction != 'O' and lab.instruction != 'Q':
        instruction_recup = input("""Ce coup ne fait pas partie de la gamme possible !
        Quel coup voulez vous jouer ? (ex : "E3" ou "N")\n...""")
        lab.instruction  = instruction_recup[0]
    instruction_recup = instruction_recup[1:]
    if instruction_recup != "":
        while True :
            try :
                instruction_recup = int(instruction_recup)
            except ValueError:
                print ("Vous devez rentrer une instruction valable cf. règles ci dessus ")
                instruction_recup = input("""Quel coup voulez vous jouer ? (ex : "E3" ou "N")\n...""")
                lab.instruction  = instruction_recup[0]
                instruction_recup = instruction_recup[1:]
                continue
            break
    else :
        instruction_recup = 1
    lab.rep_instruction = instruction_recup
    print(lab.instruction, lab.rep_instruction)

def verif_case_libre(x, y, lab):
    """Fonction qui renvoie un int en fonction de la possibilité d'écrire ou non sur la case demandé"""
    print("TEST")
    print(lab.grille_labyrinthe[y][x])
    if lab.grille_labyrinthe[y][x] == ' ':
        return 0
    elif lab.grille_labyrinthe[y][x] == '.':
        return 1
    elif lab.grille_labyrinthe[y][x] == 'U':
        return 2
    elif lab.grille_labyrinthe[y][x] == 'O':
        return 3
    else :
        return -1

def verif_coup_a_jouer(lab):
    "Fonction qui verifie si le coup est jouable, si oui elle modifie les coordonnées de robot_x robot_y"
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
        lab.rep_instruction -= 1
    print("avant = x = {}, y = {}".format(lab.robot_x, lab.robot_y))
    lab.robot_x = x
    lab.robot_y = y
    print("apres = x = {}, y = {}".format(lab.robot_x, lab.robot_y))
    print("ret {}".format(ret))
    return ret


