#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 00:25 2020
@author: nouar manelle
"""
import random

def etendue(x1, x2):
    x_etendue = relativedelta(x1, x2)
    print("Vous avez joué à ce jeu pour",abs(x_etendue.hours),"heures,",abs(x_etendue.minutes),"minutes et",abs(x_etendue.seconds),"seconds.")
    return 0

nom = input(" Quel est votre nom ? ")
print(f"Bienvenue !, {nom}!")
print(" Découvrez le jeu du Mastermind ")

while True:
    partie = input(" Avez-vous déja jouer au Mastermind ? ")
    if partie == 'oui' or partie == 'non':
        break

while True:
    while True:
        level = input(" Choisissez le level : ")
        if level == 'facile' or level == 'normal' or level == 'difficile':
            break 
################################################ Programme principal ################################################
    
longueur = '2'
nb_test = '4'
couleurs = ['bleu','rose', 'or','argent'] 
col = random.choice(couleurs)

def marstermind(pions= 2, couleurs= 4):
    tour = 1 
    L = [str(random.randint(1,couleurs)) for a in range(pions)]
    while True:
        resultat = list(L) 
        gamer = list(input("tirage" + str(tour) + ";"))
        if len(gamer) == 0:
            return "vous n'avez pas réussi"
        tour += 1 
        bien_place = 0
        mal_place = 0
        
        # la position des pions est mal placé
        for a, valeur in enumerate(gamer):
            if valeur in L:
                mal_place += 1
        # la position des pions bien placé
        for a, valeur in enumerate(gamer):
          if valeur == resultat[a]:
              bien_place += 1 
              gamer[a] = '♟'
              resultat[a] = '$'
          elif bien_place == 2: 
              return 'youpi! tu as trouvé le code'
        print(bien_place,":gagner",mal_place,":perdu")
         
marstermind()

def afficher_couleurchoisi():
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
 

def evaluation_code(code_secret, code_entree):
    bien_place, mal_place = 0, 0
    couleurs_secret = list(code_secret) 
    couleurs_choisi = list(code_entree)
        
    for v in range(len(couleurs_choisi)):    
        if couleurs_choisi[v] == couleurs_secret[v]:
            bien_place += 1
            couleurs_secret[v] = '*'
            couleurs_choisi[v] = '*'
            
    for x in range(len(couleurs_choisi)):
        if couleurs_choisi[x] in couleurs_secret and couleurs_choisi != '*':
            mal_place += 1
            c = couleurs_choisi[x]
            gamer = couleurs_secret.index(c)
            couleurs_secret[gamer] = '*'
    return [bien_place, mal_place]
    
print(evaluation_code()) 
evaluation_code()

def mettre_pions(e, col, longeur):
     e = input(" mettez vos pions : ")
     if len(e) != len(longueur):
        print(" vous n'avez mal choisi la longueur des pions ")
        return False
        for u in e :
            if u not in col : 
                return False
            else:
                return e
    
mettre_pions()

################################################ Autre programme ################################################

code_secret = input(" entrer un code secret : ")
pions = input(" entrer des pions : ")
if code_secret == pions :
    print( " mot de passe trouvé ! " )
else : 
    print("Vous avez pas trouvé le code secret ! ")



# La fonction shuffle est utilisé pour choisir une couleur aléatoire.
liste_couleurs = list(couleurs)
shuffle(liste_couleurs)
print(couleurs, liste_couleurs)

x = 0
for valeur in couleurs:
    if liste_couleurs[x] == valeur :
        print(" pion ", valeur,  " à la place ", x)
    else:
        print(" pions à la place ", x)

    x += 1

