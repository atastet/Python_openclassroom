#!/usr/bin/python3.4
# -*-coding:Utf-8

def fonction(nom, prenom, *param):
	print("J'ai recu : {}".format(param))


# test de la fonction table
if __name__ == "__main__":
    fonction("TASTET", "Anthony", 1 , 2)

