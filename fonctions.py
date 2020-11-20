import random

from donnees import *
import pickle
import os


def nom_joueur():
    test = False
    while test == False:
        try:
            nom = input("Donnez votre nom:")
            assert nom.isalpha() == True
            test = True
        except AssertionError:
            print("ce n'est pas un nom")
    return nom


def mot_au_hasard():
    """

    :rtype: str
    """
    mot = random.choice(liste_des_mots)

    return mot


def lettre_donnée() -> str:
    test = False
    while test == False:
        try:
            lettre = input("donner une lettre:")
            lettre = lettre.lower()
            assert 97 <= ord(lettre) <= 122 or (ord(lettre) == 232) or (ord(lettre) == 233)
            test = True
        except AssertionError:
            print(("Ce n'est pas une lettre"))
        except:
            print("il faut entrer une seule lettre ")
    return lettre


def lettre_dans_mot(mot, lettre: list):
    mot_masque = str()
    for i in mot:
        if i in lettre:
            mot_masque += i
        else:
            mot_masque += "*"

    return mot_masque


def enregistrer_les_scores(scores):
    fscores = open(fichier, "wb")
    monpickler = pickle.Pickler(fscores)
    monpickler.dump(scores)
    fscores.close()


def recup_scores():
    if os.path.exists(fichier):
        fscores = open(fichier, "rb")
        mondepickler = pickle.Unpickler(fscores)
        scores = mondepickler.load()
        fscores.close()
    else:
        scores = {}
    return scores
