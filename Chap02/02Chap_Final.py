# -*-coding:Utf-8 -
import time


# def mon_decorateur(ma_fonction):
#    """Mon premier décorateur"""
#
#   def fonction_modif():
#        print("Attention on appelle {}".format(ma_fonction))
#       return ma_fonction

#   return fonction_modif()


#@mon_decorateur
#def salut():
#   print("Hello you")

#salut()
#print(salut)


def control_time(nb_secs):
    """Control le temps d"une fonction. T > nb_secs ALERTE"""

    def decorateur(fonction):
        """"Decorateur appelé lors de a def de la fonction"""

        def fonction_modifiee():
            """"Fonction renvoyée par notre décorateur elle calcule le temps"""

            tmps_avant = time.time()
            valeur_renv = fonction()  # On execute la fonction
            tmps_apres = time.time()
            tmps_exec = tmps_apres - tmps_avant
            if tmps_exec >= nb_secs:
                print("La fonction a pris plus de temps que prévu {} secs".format(tmps_exec))
            else :
                print("OK")
            return valeur_renv
        return fonction_modifiee()
    return decorateur

print("HELLO")

@control_time(0.00000000001)
def attendre_until():
    """Attendre jusqu'à ce qu'un input arrive"""

    n = 0
    while n < 10000:
        n +=1
     #input("appuyer sur une touche")


#attendre_until()
