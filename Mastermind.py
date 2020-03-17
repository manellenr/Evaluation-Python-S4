#importation de la bibliothèque random pour le tirage aléation du code secret
import random, sys
#création d'une fonction mastermind qui par defaud à quatres chiffres du code secret à trouver et 6 couleurs
def marstermind(pions= 2, couleurs= 4):
    i = 1 # premier tirage
    secret = [str(random.randint(1,couleurs)) for i in range(pions)]
# le programme  tire un entier aléatoire en 1 et 4 couleurs et il répète ca 2 fois car ont à définit 2 pions
#on fait une boucle while qui se répète à l'infini
    while True:
        resultat = list(secret) 
        gameur = list(input("tirage" + str(i) + ";"))#mettre une chaine de caractères en liste
#faut configurer si la personne ne trouve pas le code
        if len(gameur) == 0:
            return "vous n'avez pas réussit"
        i += 1 #pour recommencer un nouveau tirage si le joueur n'a pas réussit
#ensuite on va compter les pions bien placer et mal placé mais on les initiales à zéro vu que la partie à pas débuter
        bien_place, mal_place = 0,0
        for a, valeur in enumerate(gameur):# pour savoir la position des pions est mal placé
            if valeur in secret:# si le pion est mal placé dans le code a initialisé à zéro
                mal_place += 1#si le nombre est mal placé on augmente de 1 pour continuer à trouver les autres pions
                secret[secret.index(valeur)] = '$'#trouver le rang de la valeur dans le code qui sera remplacé par un dollar
        for b, valeur in enumerate(gameur):# pour savoir la position des pions est bien placé
          if valeur == resultat[b]: # si le pion est bien placé dans le code b initialisé à zéro
              bien_place += 1 #si le nombre est bien placé on augmente de 1 pour continuer à trouver les autres pions
              gameur[i] = '♟'#on remplace le joueur par un symbole
              resultat[i] = '$'
          if  bien_place == 2: #si on à 2 pions bien placé on gagne 
              return 'youpi! tu as trouvé le secret'
        print(bien_place,":gagner",mal_place,":perdu")
         
marstermind()        

longueur = 2
nb_tentative = 4 #4 tentatives maximum pour trouver le code secret
couleurs = ['bleu','rose','rouge','jaune']#liste des couleurs possibles
col = [couleurs[i][0] for i in range(len(couleurs))]

def afficher_couleurchoisi():
    for i in couleurs: #on va chercher les couleurs dans la liste
        print(i)
afficher_couleurchoisi()

def result_secret():
    code = '' #le résultat secret renvoie une chaine de chractère
    return code    
result_secret()
