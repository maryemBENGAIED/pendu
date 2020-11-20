from donnees import *
from fonctions import *

scores = recup_scores()
nom = nom_joueur()

if nom not in scores.keys():
    scores[nom] = 0

rejouer = True

while rejouer:
    print("Joueur {0}: {1} point(s)".format(nom, scores[nom]))
    mot = mot_au_hasard()
    lettres = []
    mot_masq = lettre_dans_mot(mot, lettres)
    vies = chances

    while vies > 0 and mot_masq != mot:
        print("Mot à trouver {0} (encore {1} chances)".format(mot_masq, vies))
        lettre = lettre_donnée()
        if lettre in lettres:
            print("Lettre déjà saisie")
        elif lettre in mot:
            print("Bon choix")
            lettres.append(lettre)
        else:
            print("Mauvais choix")
            vies -= 1
        mot_masq = lettre_dans_mot(mot, lettres)

    if mot_masq == mot:
        print("Félicitations! Le mot est {0}".format(mot))
    else:
        print("Loser!")
    scores[nom] += vies

    test = True
    while test:
        try:
            question = input("Souhaitez-vous continuer la partie (O/N) ?")
            question = question.lower()
            assert question == 'n' or question == 'o'
            test = False

        except AssertionError:
            print("Répondez par o ou n")
    if question == 'n':
        rejouer = False
enregistrer_les_scores(scores)

print("Vous finissez la partie avec {0} points.".format(scores[nom]))
