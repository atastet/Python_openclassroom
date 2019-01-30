# -*-coding:Utf-8 -*

import re

chaine = ""
exp = r"^0[0-9]([ .-]?[0-9]{2}){4}$"
while re.search(exp, chaine) is None:
    raw_input("Numero")