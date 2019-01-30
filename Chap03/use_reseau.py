# -*-coding:Utf-8 -*

#protocole TCP s'assure de la bonne reception des infos par la cible contrairement au UDP
#TCP plus fiable mais plus lent

import socket

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(connexion_principale)
connexion_principale.bind(('', 12800)) #On configure un port pour pouvoir communiquer et un nom d'hote vide
connexion_principale.listen(5) #On autorise 5 clients à se connecter
connexion_client, infos_connexion = connexion_principale.accept()
print(infos_connexion)
connexion_client.send(b"je viens de t'accepter")
connexion_client.close()