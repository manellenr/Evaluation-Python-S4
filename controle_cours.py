# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:30:47 2020

@author: nouar manelle
"""


# q 1
def sup21(n):
    if n >= 21:
        return True
    else:
        return False
sup21(21)
print(sup21(21))
sup21(2)
print(sup21(2))

# q 2
def pairs( listes):
     l = [i for i in listes if i%2== 0]
     return l
pairs([1,2,3])
print(pairs([1,2,3]))

# q 3

def ajout4(liste):
    res = liste + [4]
    return res
l = [1,2,3]
print(ajout4(l))
print(ajout4([]))
print(ajout4([1,2,4]))

# q 4
def to_strings(d):
    l = []
    for x, y in d.items():
       l.append(str(x) +":"+ str(y))
       print(l)
    return l
print(to_strings({1:2,3:4}))


# q 5
def extremites(li):
    l1 = li[-2:]
    l2 = li[:2]  
    res = l1 + l2
    return res
extremites(['a', 'b', 'c', 'd', 'e'])
print(extremites(['a', 'b', 'c', 'd', 'e']))

# q 6
class Mot():
    def __init__ (self, mot):
        self.mot = mot
    def mot(self, mot):
        self.mot = mot
    def comptelettre(self, lettre, mot):
        self.letter = lettre.lower
        for lettre in mot:
            if lettre.lower() in mot.lower():
                print(self.count(lettre.lower()))
            
mot = Mot('Bonjour')
mot.comptelettre('B') == mot.comptelettre('b') == 1


# q 7       
def tri_et_inverse(l):
    return (sorted(l), reversed(l))
maliste = [4,7,6]
print(maliste)
tri_et_inverse(maliste)


  
# q 9
ville_nom_pays = {'Paris':'France','Berlin':'Allemagne','Madrid':'Espagne','Moscou':'Russie'} 

# q 10
import doctest

class Pays():
    def __init__ (self, nom, visa):
        self.nom = nom
        self.visa = visa
ville_pays = {'Paris' : Pays('France', False),'Berlin' : Pays('Allemagne', False),'Madrid' : Pays('Espagne', False),'Moscou' : Pays('Russie', True)}

if __name__ == "__main__":
    doctest.testmod(verbose=True)
