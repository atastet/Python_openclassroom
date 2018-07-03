#!/usr/bin/python3.4
# -*-coding:Utf-8

prenoms = ["Anthony", "Mathilde", "Simon", "Mateu", "Ugo"]
prenoms.sort()
print(prenoms)

list_prenoms = ["Anthony", "Mathilde", "Simon", "Mateu", "Ugo"]
s_prenom = sorted(list_prenoms)
print(s_prenom)
print(list_prenoms)

etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]
print(sorted(etudiants))

print(sorted(etudiants, key=lambda colonne : colonne[2]))
