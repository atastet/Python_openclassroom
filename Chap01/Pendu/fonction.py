#!/usr/bin/python3.4
# -*-coding:Utf-8

from donnees import *
import pickle 
from random import randrange
import os

def get_pseudo(): 
	try : 
		pseudo = input("Rentrez votre pseudo...")
		return pseudo
	except NameError :
		print("Votre pseudo doit être une chaine de caractere")

def load_scores():
	if os.path.exists(nom_fichier_score):
		fichier_scores = open(nom_fichier_score, "rb")
		mon_depickler = pickle.Unpickler(fichier_scores)
		scores = mon_depickler.load()
		fichier_scores.close()
	else :
		scores = {}
	return scores

def get_word():
	num = randrange(20)
	return liste_mots[num]

def get_string_ans(word):
	size = len(word)
	i = 0
	string = "*"
	while i < size :
		string = string + "*"
		i += 1
	return (string)

def get_letter():
	lettre = input("Tapez une lettre: ")
	lettre = lettre.lower()
	if len(lettre)>1 or not lettre.isalpha():
		print("Vous n'avez pas saisi une lettre valide.")
		return get_letter()
	else:
		return lettre

def	check_if_letter_ok(word, letter, nb_coup, answer_string):
	if word.find(letter) == -1 :
		print("Nope {} n'est pas dans ce mot".format(letter))
		nb_coup -= 1
		return answer_string, nb_coup
	else :
		print("GREAT {} est dans le mot".format(letter))
		position = word.find(letter)
		answer_string = list(answer_string)
		answer_string[position] = letter
		''.join(answer_string)
		return answer_string, nb_coup
