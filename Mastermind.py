# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 00:25 2020
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
        # faut configurer pour voir si la personne ne trouve pas le code
        if len(gamer) == 0:
            return "vous n'avez pas réussi"
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
          elif bien_place == 2: 
              return 'youpi! tu as trouvé le secret'
        print(bien_place,":gagner",mal_place,":perdu")
         
marstermind()       

# test
print( list(enumerate('32') ) )
print( list(enumerate('12') ) )

longueur = 2
nb_test = 4
couleurs = ['bleu','rose', 'or','argent'] # liste des choix de couleurs possibles
col = []
for i in couleurs :
    col.append(i[0])

def afficher_couleurchoisi():
    for i in couleurs: # on va chercher les couleurs dans la liste
        print(i)
print(afficher_couleurchoisi())

afficher_couleurchoisi()

def result_secret():
    code_secret = " " # le résultat secret renvoie une chaine de charactères
    for i in range(0,longueur):
        position_nb = random.randint(0,len(col) - 1)
        code_secret = col[position_nb] + code_secret
    return code_secret    

# test
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

# test
    
print(evaluation_code('br','br')) # affiche [2, 2]
print(evaluation_code('br','bo')) # affiche [1, 1]
print(evaluation_code('rb','oa')) # affiche [0, 0]
print(evaluation_code('rb','rb')) # affiche [2, 2]

evaluation_code()

def  mettre_pions():
    e = input("mettez vos pions : ")
    if len(e) != len(longueur):
        print("vous n'avez mal choisi la longueur des pions ")
        return False
    for u in e :
        if u not in col : 
            return False
    else:
        return e
# test
print(mettre_pions())

mettre_pions()

# on veut un binome de deux pions  
res = result_secret()
binome = "False"
for x in range(nb_test):
while binome == "False" :
    binome = mettre_pions()
r = evaluation_code(binome,res)
if r[0] == 2 :
    print (" vous avec réussi le Mastermind ")
j += r[0]
else :
    print(" Vous avez échoue :",j)


