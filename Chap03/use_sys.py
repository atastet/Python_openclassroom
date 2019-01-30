# -*-coding:Utf-8 -*

import sys
import signal
import argparse
import os

print(sys.stdin)# L'entrée standard (standard input)
print(sys.stdout) # La sortie standard (standard output)
print(sys.stderr) # L'erreur standard (standard error)

fichier = open("Sortie_test.txt", 'w')
sys.stdout = fichier
sys.stdout.write("Hello")
print("Hello Bis\n")
sys.stdout = sys.__stdout__
print("Now it is out")

#Signaux
print ("SIGINT = {} ".format(signal.SIGINT))

def fermer_pgm(signal, frame):
    print("ADIOS")
    sys.exit(0)

signal.signal(signal.SIGINT, fermer_pgm)
#while True:
 #   print("Boucle")
  #  continue

#ARG

print(sys.argv)
parser = argparse.ArgumentParser()
#parser .add_argument("x", help="Mettre le nombre au carré")
print(parser.parse_args())

#Commande sys
print(os.system("ls"))
print(os.popen("sleep 0.5")) #Execute et met en pause
print("TEST")