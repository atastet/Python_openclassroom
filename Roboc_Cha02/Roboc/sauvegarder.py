# -*-coding:Utf-8 -*

import pickle

def make_sauvegarde(lab):
    with open('sauvegarde',"wb") as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(lab)
        print("SAUVEGARE OK")

def recup_sauvgarde():
    with open('sauvegarde','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        lab_recup = mon_depickler.load()
        print ("SAUVEGARDE RECUPEREE")
    return lab_recup