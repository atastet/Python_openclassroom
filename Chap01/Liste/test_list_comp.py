#!/usr/bin/python3.4
# -*-coding:Utf-8

liste_start = [1, 2, 3, 4, 5, 6]
liste_2 = [nb * nb for nb  in liste_start]
print(liste_2)
print("vs {} !".format(liste_start))

# Filtrer

liste_3 = [nb for nb in liste_start if nb % 2 == 0]
print(liste_3)
