#!/usr/bin/python3.4
# -*-coding:Utf-8 -

def mlt_tbl(nb):
	"""Fonction affichant lq tqble de multuplication de nb
	nb étant > 0"""
	i = 1
	maxi = 10
	if nb <= 0:
		print("Nb must be positive")
	while i < 10 :
		print(nb, "x ", i, "=", i * nb)
		i += 1

ip = input("Table de multiplication de ...")
int(ip)
mlt_tbl(ip)

	

