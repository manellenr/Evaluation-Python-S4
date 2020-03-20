from Mastermind import doctest
import doctest_private_tests_external
from random import shuffle

#import doctest
################################################ #Doctests ################################################

# doctest testmod
class level:
    """
    Cette classe permet de créer les différents levels
    """
    def __init__(self, niveau):
        self.niveau = niveau
        self.debut = 0
    
    def prog(self):
      """
      on veut programmer les niveaux
      et les afficher. 
      """   
      pass
    
    
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

    doctest.testmod()
    
# doctest hashed values
couleurs = ['bleu','rose', 'or','argent']
print('dict:', {x: len(x) for x in couleurs})
print('set :', set(couleurs))

# doctest private tests
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
liste_couleurs = list(couleurs)
shuffle(liste_couleurs)
print(couleurs, liste_couleurs)


# analyse des bien placé et mal placée
x = 0
for valeur in couleurs:
    if liste_couleurs[x] == valeur :
        print(" pion ", valeur,  " à la place ", x)
    else:
        print(" pions à la place ", x)

    x += 1

