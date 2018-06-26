#!/usr/bin/python3.4
# -*-coding:Utf-8

def decomposer(entier, div_par):
	p_e = entier // div_par
	reste = entier % div_par
	return p_e, reste
