#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 00:25 2020
@author: nouar manelle
"""
################################################ Programme principal ################################################

import random
from random import shuffle

print(" Bienvenue ! ")
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
        print(" Changer de niveau : ")

# création d'une fonction mastermind qui par defaud à quatres chiffres du code secret à trouver et 4 couleurs

def marstermind(pions= 2, couleurs= 4):
    i = 1 
    secret = [str(random.randint(1,couleurs)) for i in range(pions)]
    while True:
        resultat = list(secret) 
        gamer = list(input("tirage" + str(i) + ";"))
        # faut configurer pour voir si la personne ne trouve pas le code
        if len(gamer) == 0:
            return "vous n'avez pas réussi"
        i += 1 

        # ensuite on va compter les pions bien placer et mal placé mais on les initiales à zéro vu que la partie à pas débuter
        bien_place = 0
        mal_place = 0
        
        # la position des pions est mal placé
        for a, valeur in enumerate(gamer):
            if valeur in secret:
                mal_place += 1
                secret[secret.index(valeur)] = '$'
        # la position des pions bien placé
        for b, valeur in enumerate(gamer):
          if valeur == resultat[b]:
              bien_place += 1 
              gamer[i] = '♟'
              resultat[i] = '$'
          elif bien_place == 2: 
              return 'youpi! tu as trouvé le secret'
        print(bien_place,":gagner",mal_place,":perdu")
         
marstermind()       

longueur = 2
nb_test = 4
couleurs = ['bleu','rose', 'or','argent'] # liste des choix de couleurs possibles
col = []
for i in couleurs :
    col.append(i[0])

def afficher_couleurchoisi():
    for i in couleurs:
        print(i)
print(afficher_couleurchoisi())

afficher_couleurchoisi()

def result_secret():
    code_secret = " " # le résultat secret renvoie une chaine de charactères
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
    
print(evaluation_code('br','br')) # affiche [2, 2]
print(evaluation_code('br','bo')) # affiche [1, 1]
print(evaluation_code('rb','oa')) # affiche [0, 0]
print(evaluation_code('rb','rb')) # affiche [2, 2]

evaluation_code('br','br') 

def  mettre_pions():
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

################################################ Doctests ################################################

# doctest testmod
class marstermind(object):
    """
    cette classe nous donne les différentes
    pions qui sont déja placé dans le jeu
    """
    pass
    
    def afficher_couleurchoisi(self):
        """
        retourne un objet qui est la couleur 
        qu'on a choisi        
        """
        pass
    
    afficher_couleurchoisi.__doc__
    help(afficher_couleurchoisi)
    
    def result_secret(self):
        """
        retourne un objet qui représente le 
        code secret du mastermind
        """
        pass
    
    result_secret.__doc__
    help(result_secret)
    
    def evaluation_code(self,code_secret, code_entree):
        """
        entrer un code et vérifier si c'est le bon code
        secret.
        """
        self.position = (code_secret, code_entree)
    def __str__(self):
        return f"code indéfinie de position {self.position}" 
    
    evaluation_code.__doc__ 
    help(evaluation_code)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
# doctest hashed values

print('dict:', {x: len(x) for x in couleurs})
print('set :', set(couleurs))

# doctest private tests
import doctest_private_tests_external

__test__ = {
    'numbers': """
>>> evaluation_code('br','br') 
[2, 2]

>>> evaluation_code('br','bo')
[1, 1]
""",

    'external': doctest_private_tests_external,
}
    
################################################ Tests unitaires ################################################
    
import unittest

# unittest truth 
class jeu(unittest.TestCase):

    def testAssertTrue(self):
        self.assertTrue(True, ' Vous avez gagné le jeu :) ')

    def testAssertFalse(self):
        self.assertFalse(False, ' vous avez perdu le jeu :(')
        
################################################ Autres tests ################################################

code_secret = input(" entrer un code secret : ")
pions = input(" entrer des pions : ")
if code_secret == pions :
    print( " mot de passe trouvé ! " )
else : 
    print("Vous avez pas trouvé le code secret ! ")



# couleurs aléatoire  
shuffle(liste_couleurs)
print(couleurs, liste_couleurs)
liste_couleurs = list(couleurs)

# analyse des bien placé et mal placée
x = 0
for valeur in couleurs:
    if liste_couleurs[x] == valeur :
        print(" pion ", valeur,  " à la place ", x)
    else:
        print(" pions à la place ", x)

    x += 1

