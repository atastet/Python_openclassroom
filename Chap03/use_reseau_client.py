# -*-coding:Utf-8 -*

import socket
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connexion_avec_serveur.connect(('localhost', 12800))
msg_recu = connexion_avec_serveur.recv(1024)
print(msg_recu)
connexion_avec_serveur.close()