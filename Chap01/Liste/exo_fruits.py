#!/usr/bin/python3.4
# -*-coding:Utf-8

inventaire = [("pommes", 22), ("melons", 4), ("poires", 18), ("fraises", 76), ("prunes", 51),]

inventaire_3 = [tuple(reversed(tu)) for tu in inventaire]
inventaire_2 = sorted(inventaire_3)
print(inventaire_2)
