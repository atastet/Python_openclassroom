#!/usr/bin/python3.4
# -*-coding:Utf-8

fichier = open("fichier.txt", "w")
fichier.write("ON ECRASE TOUT")
fichier.close()
fichier = open("fichier.txt", "r")
contenu = fichier.read()
fichier.close()
print(contenu)
