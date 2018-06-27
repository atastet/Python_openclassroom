#!/usr/bin/python3.4
# -*-coding:Utf-8

from donnees import *
from fonction import *

pseudo = get_pseudo()
scores = load_scores()

if pseudo not in scores.keys():
	scores[pseudo] = 0

stopper = 'o'

while stopper != 'n' :
	nb_coup = 8 
	word = get_word()
	answer_string = get_string_ans(word) 
	while ((nb_coup > 0) and answer_string.find('*') != -1):
		letter = get_letter()
		answer_string, nb_coup = check_if_letter_ok(word, letter, nb_coup, answer_string)
	print("Choisi une nouvelle lettre ... on est à {}".format(answer_string)) 
	print(scores[pseudo])
	print(answer_string)
	print(word)
