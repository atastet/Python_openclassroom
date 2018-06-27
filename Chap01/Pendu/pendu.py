#!/usr/bin/python3.4
# -*-coding:Utf-8

from donnees import *
from fonction import *

pseudo = get_pseudo()
scores = get_scores()

if pseudo not in scores.keys():
	scores[pseudo] = 0

stopper = 'o'

while stopper != 'n' :
	nb_coup = 8 
	word = get_word()
	answer_string = get_string_ans(word) 
	letter_liste = []
	while ((nb_coup > 0) and answer_string.find('*') != -1):
		print("Current state = {}".format(answer_string))
		letter = get_letter(letter_liste)
		letter_liste.extend(letter)
		print(answer_string)
		print(word)
		print(letter_liste)
		answer_string, nb_coup = check_if_letter_ok(word, letter, nb_coup, answer_string)
	if nb_coup == 0 :
		stopper = input("Dommage ... c'est perdu. o pour continuer n pour quitter o/n")
		stopper.lower()
	else :
		stopper = input("Excellent ! Veux tu continuer ? o/n")
		scores[pseudo] += nb_coup
	print("Ton score est de {}".format(scores[pseudo]))

save_score(scores, pseudo)
print("Partie termine avec {} points".format(scores[pseudo]))
