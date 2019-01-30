# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""
import os

from cartes_base_code import Carte
from labyrinthe_base_code import Labyrinthe
from coups_a_jouer import *

# On charge les cartes existantes
cartes = []
mes_fichiers = []

for mon_fichier in os.listdir("cartes"):
    if mon_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", mon_fichier)
        mes_fichiers.append(mon_fichier)
        nom_carte = mon_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            cartes.append(contenu)
        # Création d'une carte, à compléter

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {} \n{}".format(i + 1,mes_fichiers[i][:-4].upper(),cartes[i]))

#On demande à l'utilisateur de rentrer le labyrinthe qu'il veut utiliser

labyrinthe_choice = input("Entrez le numéro de labyrinthe sur lequel vous voulez jouer :\n...")
lab_choice = 0

#On vérifie que la valeur entrée soit bien un int et si le labyrinthe existe

while lab_choice == 0:
    try :
        lab_choice =int(labyrinthe_choice)
    except ValueError:
        print("Vous devez entrez un chiffre entre : 1 et {}\n".format(i+1))
        labyrinthe_choice = input("\nEntrez un numéro de labyrinthe sur lequel vous voulez jouer ...")
        continue
    while lab_choice < 1 or lab_choice > (i + 1):
        print("Ce labyrinthe n'existe pas !\n")
        labyrinthe_choice = input("\nEntrez un numéro de labyrinthe sur lequel vous voulez jouer entre : 1 et {}\n".format(i+1))
        lab_choice = int(labyrinthe_choice)

#On transforme l'input avec le vrai nom du fichier dans notre repo
print(lab_choice)
labyrinthe_fichier = mes_fichiers[lab_choice - 1]
labyrinthe_str = cartes[lab_choice-1]


print("OK on va pouvoir jouer sur le labyrinthe niveau : {0}\n\n---{1}----\n\n{2}".format(labyrinthe_fichier[:-4],labyrinthe_fichier[:-4].upper(), labyrinthe_str))

#On va créer la map grâce à la class Carte qui va nous passer d'une string à un tableau

my_map = Carte(labyrinthe_fichier[:-4], labyrinthe_str)

#On créer une classe qui enregistre la position du robot et la grille
my_lab = Labyrinthe(my_map)
print(my_lab.robot_y, my_lab.robot_x, my_lab.grille_labyrinthe)

#On va récupérer le premier coup à jouer
print("""Le robot est contrôlable grâce à des commandes entrées au clavier. Il doit exister les commandes suivantes :
- Q qui doit permettre de sauvegarder et quitter la partie en cours ;
- N qui demande au robot de se déplacer vers le nord (c'est-à-dire le haut de votre écran) ;
- E qui demande au robot de se déplacer vers l'est (c'est-à-dire la droite de votre écran) ;
- S qui demande au robot de se déplacer vers le sud (c'est-à-dire le bas de votre écran) ;
- O qui demande au robot de se déplacer vers l'ouest (c'est-à-dire la gauche de votre écran) ;
- Chacune des directions ci-dessus suivies d'un nombre permet d'avancer de plusieurs cases (par exemple E3 pour avancer de trois cases vers l'est).""")
recup_coup_a_jouer(my_lab)
#SUPPRIMER A LA FIN
print(my_lab.rep_instruction, my_lab.instruction)
while verif_coup_a_jouer(my_lab) == -1:
    print("Ce coup est impossible votre robot ne peut pas se déplacer ainsi")
    print(verif_coup_a_jouer(my_lab))
    recup_coup_a_jouer(my_lab)
#On sauvegarde
# ... Complétez le programme ...
