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

def get_scores():
	if os.path.exists("score"):
		fichier_scores = open("score", "rb")
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
	while i < size - 1 :
		string = string + "*"
		i += 1
	return (string)

def get_letter(letter_liste):
	lettre = input("Tapez une lettre: ")
	if len(lettre)>1 or not lettre.isalpha():
		print("Vous n'avez pas saisi une lettre valide.")
		return get_letter(letter_liste)
	else:
		if lettre in letter_liste :
			print("{} déjà rentre...".format(lettre))
			return get_letter(letter_liste)
	return lettre

def get_letter_out(word, letter, position):
		word = list(word)
		word[position] = '$'
		word_modif = ''.join(word)
		return word_modif

def check_if_letter_ok(word, letter, nb_coup, answer_string):
	if word.find(letter) == -1 :
		print("Nope {} n'est pas dans ce mot".format(letter))
		answer_modif = answer_string
		nb_coup -= 1
	else :
		while word.find(letter) != -1 :
			print("GREAT {} est dans le mot".format(letter))
			position = word.find(letter)
			word = get_letter_out(word, letter, position)
			answer_string = list(answer_string)
			answer_string[position] = letter
			answer_modif = ''.join(answer_string)
	return answer_modif, nb_coup

def save_score(scores, pseudo):
	fichier_scores = open("score", "wb") # On écrase les anciens scores
	mon_pickler = pickle.Pickler(fichier_scores)
	mon_pickler.dump(scores)
	fichier_scores.close()
