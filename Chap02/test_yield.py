#!/usr/bin/python3.4
# -*-coding:Utf-8

def mongenerateur():
	yield 1
	yield 2
	yield 3

my_iter = iter(mongenerateur())
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

def intervalle(borne_inf, borne_sup):
	"""Générateur parcourant la série des entiers entre borne_inf et borne_sup.
	Note: borne_inf doit être inférieure à borne_sup"""
	borne_inf += 1
	while borne_inf < borne_sup:
		yield borne_inf
		borne_inf += 1
for nombre in intervalle(15, 18):
	print(nombre)
