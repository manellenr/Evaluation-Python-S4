# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:36:00 2020
@author: nouar manelle
"""
import random
# création d'une fonction mastermind qui par defaud à quatres chiffres du code secret à trouver et 6 couleurs

def marstermind(pions= 2, couleurs= 4):
    i = 1 
    secret = [str(random.randint(1,couleurs)) for i in range(pions)]
    while True:
        resultat = list(secret) 
        gamer = list(input("tirage" + str(i) + ";"))
        # faut configurer si la personne ne trouve pas le code
        if len(gamer) == 0:
            return "vous n'avez pas réussit"
        i += 1 

        # ensuite on va compter les pions bien placer et mal placé mais on les initiales à zéro vu que la partie à pas débuter
        bien_place, mal_place = 0,0
        
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
          if  bien_place == 2: 
              return 'youpi! tu as trouvé le secret'
        print(bien_place,":gagner",mal_place,":perdu")
         
marstermind()       

# test
print( list(enumerate('32') ) )
print( list(enumerate('12') ) )

longueur = 2
nb_tentative = 4

# liste des choix de couleurs possibles
couleurs = ['bleu','rose', 'or','argent'] 

col = []
for i in couleurs :
    col.append(i[0])

# on va chercher les couleurs dans la liste
def afficher_couleurchoisi():
    for i in couleurs: 
        print(i)
print(afficher_couleurchoisi())

# le résultat secret renvoie une chaine de charactères
def result_secret():
    code_secret = " " 
    for i in range(0,longueur):
        position_nb = random.randint(0,len(col) - 1)
        code_secret = col[position_nb] + code_secret
    return code_secret    

# test
print(result_secret())


def evaluation_code(code_secret, code_entree):
    bien_place = 0
    mal_place = 0
    couleurs_secret = list(code_secret)
    couleurs_choisi = list(code_entree)
        
    for v in range(len(couleurs_choisi)):    
        if couleurs_choisi[v] == couleurs_secret[v]:
            bien_place += 1
            couleurs_secret[v] = '*'
            couleurs_choisi[v] = '*'
    return [bien_place, mal_place]

# test   
print(evaluation_code('br','oa'))
print(evaluation_code('or','ba'))
print(evaluation_code('ar','ba'))
