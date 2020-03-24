#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 00:25 2020
@author: nouar manelle
"""
################################################ Programme principal ################################################


import random

# Non ca c'est dans if __name__ == __main__
print(" Bienvenue ! ")
print(" Découvrez le jeu du Mastermind ")

while True:
    partie = input(" Avez-vous déja jouer au Mastermind ? ")
    if partie == "oui" or partie == "non":
        break

while True:  # superfliu
    while True:
        level = input(" Choisissez le level : ")
        if level == "facile" or level == "normal" or level == "difficile":
            break

longueur = "2"
nb_test = "4"  # ???
couleurs = ["bleu", "rose", "or", "argent"]
col = random.choice(couleurs)


def marstermind(pions=2, couleurs=4):  # pions=longueur et coutleurs = couleurs non
    tour = 1
    L = [str(random.randint(1, couleurs)) for a in range(pions)]
    # Bah non vous réinventez la roue.
    while True:
        resultat = list(L)  # Interet "
        gamer = list(
            input("tirage" + str(tour) + ";")
        )  # ????? ça ne vaudra jamais a la ligne du dessous

        if len(gamer) == 0:
            return "vous n'avez pas réussi"
        tour += 1
        bien_place = 0
        mal_place = 0
        # de ici
        # la position des pions est mal placé
        for a, valeur in enumerate(gamer):
            if valeur in L:
                mal_place += 1
        # la position des pions bien placé
        for a, valeur in enumerate(gamer):
            if valeur == resultat[a]:
                bien_place += 1
                gamer[a] = "♟"  #
                resultat[a] = "$"
            elif bien_place == 2:
                return "youpi! tu as trouvé le code"
        # à la c'esrt un fonction que vous devez ecrite et utiliser.
        print(bien_place, ":gagner", mal_place, ":perdu")


marstermind()  # __name__ == '__main__'


def afficher_couleurchoisi():  # ça ca a toute sa place dans une doctring mais faites plutot des test unitaires.
    for i in couleurs:
        print(i)


print(afficher_couleurchoisi())

afficher_couleurchoisi()


def result_secret():
    code_secret = " "
    for i in range(longueur):
        position_nb = random.randint(0, len(col) - 1)
        code_secret = col[position_nb] + code_secret
    return code_secret


print(result_secret())

result_secret()

# Pourquoi dupliqueer aurant de code .....


def evaluation_code(code_secret, code_entree):
    bien_place, mal_place = 0, 0
    couleurs_secret = list(code_secret)
    couleurs_choisi = list(code_entree)

    for v in range(len(couleurs_choisi)):
        if couleurs_choisi[v] == couleurs_secret[v]:
            bien_place += 1
            couleurs_secret[v] = "*"
            couleurs_choisi[v] = "*"

    for x in range(len(couleurs_choisi)):
        if couleurs_choisi[x] in couleurs_secret and couleurs_choisi != "*":
            mal_place += 1
            c = couleurs_choisi[x]
            gamer = couleurs_secret.index(c)
            couleurs_secret[gamer] = "*"
    return [bien_place, mal_place]


# voila ca c'st pas mal une contion qui renvoie quelque chose que vous pouvez tester

print(evaluation_code())
evaluation_code()


# nommez vos variables correctectement.


def mettre_pions(e, col, longeur):
    e = input(" mettez vos pions : ")
    if len(e) != len(longueur):
        print(" vous n'avez mal choisi la longueur des pions ")
        return False
        for u in e:
            if u not in col:
                return False
            else:
                return e


mettre_pions()  # ceci ne risque pas de fonctionner.
