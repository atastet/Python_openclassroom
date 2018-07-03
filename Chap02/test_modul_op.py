#!/usr/bin/python3.4
# -*-coding:Utf-8 -


etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

from operator import itemgetter
print(sorted(etudiants, key=itemgetter(2)))
