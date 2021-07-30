import os
import random

def dictionnaire():
    with open("dico.txt","r+") as dico:
            liste = dico.readlines()
            choix = random.choice(liste)
    return choix

def mystere(choix):
    taille = len(choix)
    print(taille)

