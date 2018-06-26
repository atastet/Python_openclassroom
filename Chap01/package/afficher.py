#!/usr/bin/python3.4
# -*-coding:Utf-8 -

def afficher(*values, sep=' ', end='\n'):
	 """Fonction chargée de reproduire le comportement de print.
    
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés. 
    On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :

    print(chaine, end='')"""
	liste = list(values)
	for i, values in enumerate(values):
		values[i] = str(values[i])
	string = sep.join(liste)
	string += fin
	return string	
