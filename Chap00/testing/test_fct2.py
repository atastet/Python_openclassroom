#!/usr/bin/python3.4
# -*-coding:Utf-8 -
i= 2

def exemple():
    print(i, "Un exemple d'une fonction sans paramètre")

exemple()

def exemple(): # On redéfinit la fonction exemple
    print("Un autre exemple de fonction sans paramètre")

exemple()
