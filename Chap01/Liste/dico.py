#!/usr/bin/python3.4
# -*-coding:Utf-8

echec = {('A', 1):"Pion blanc", ('B', 2):"Tour Noire"}
print(echec[('A', 1)])
del echec[('A', 1)]
print(echec)
string = echec.pop(('B', 2))
print(string)
print("dico is now {}".format(echec))
