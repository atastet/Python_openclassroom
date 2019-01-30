# -*-coding:Utf-8 -*

from getpass import getpass
import hashlib

mdp = getpass("Tappez mdp :")
print("Je l'imprime ".format(mdp))

#HASH
print(hashlib.algorithms_guaranteed)
#sha1 ne prend que des chaine de bits
chaine_bits = b"mdp"
print(chaine_bits)
mdp = hashlib.sha1(b"mdp")
print(mdp.hexdigest())
