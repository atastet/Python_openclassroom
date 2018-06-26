#!/usr/bin/python3.4
# -*-coding:Utf-8

liste = [1, 2, 3]

liste2 = list(liste)
liste2.append(4)
print("liste = {}, liste2 = {}".format(liste, liste2))
print("id liste = {}, id liste2 = {}".format(id(liste), id(liste2)))
liste2 = liste
print("id liste = {}, id liste2 = {}".format(id(liste), id(liste2)))
