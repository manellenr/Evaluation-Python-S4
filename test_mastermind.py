from Mastermind import doctest
import doctest_private_tests_external
from random import shuffle
import unittest

# doctest testmod   

class level:
    def __init__(self):
        print("init")
    def __call__(self):
        print("call")
        
class marstermind():
    """
    Classe du jeu
    """
    pass
    
    def afficher_couleurchoisi(self):
        """
        Classe choix aléatoire de la couleur        
        """
        pass
    
    afficher_couleurchoisi.__doc__
    help(afficher_couleurchoisi)
    
    def result_secret(self):
        
        pass
    
    result_secret.__doc__
    help(result_secret)
    
    def evaluation_code(self,code_secret, code_entree):
        """
        Evalution combinaisn
        secret.
        """
        self.position = (code_secret, code_entree)
    def __str__(self):
        return f"code indéfinie de position {self.position}" 
    
    evaluation_code.__doc__ 
    help(evaluation_code)
    
def main():
    print ("Bienvenue")
    if __name__ == '__main__':
        doctest.testmod()
main()
        
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
  

# unittest truth 
class jeu(unittest.TestCase):

    def testAssertTrue(self):
        self.assertTrue(True, ' Vous avez gagné le jeu :) ')

    def testAssertFalse(self):
        self.assertFalse(False, ' vous avez perdu le jeu :(')
        
if __name__ == '__main__':
    unittest.main()

class testerlejeu(unittest.TestCase):
    
    def sortieverificateur(self):
        pb = ['bleu','rose', 'or','argent'] 
        solution = pb
        self.assertEqual(mastermind.check(pb, solution), (4, 0))
    
     def generersolution(self):
        solution = mastermind.generateProblem()
        self.assertEqual(len(solution), 2)
        
    def testersortie(self):
        pb = ['b','r']
        solution = ['o', 'b']
        self.assertEqual(mastermind.check(pb, solution), (0, 2))

if __name__ == '__main__':
    unittest.main()

