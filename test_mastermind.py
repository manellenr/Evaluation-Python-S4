from mastermind import doctest
import doctest_private_tests_external
from random import shuffle

# import doctest
################################################ #Doctests ################################################

# doctest testmod


# a quoi sert cette classe ?


class level:
    def __init__(self):
        print("init")

    def __call__(self):
        print("call")


class marstermind:  # du coup Mastermind dans le fichier mastermind.py

    """
    Classe du jeu
    """

    pass

    def afficher_couleurchoisi(self):
        """
        Classe choix aléatoire de la couleur
        """
        pass

    afficher_couleurchoisi.__doc__  # ? Faites vous un fichier a coté vouspolluez beaucoup le code
    help(afficher_couleurchoisi)  # ? ou alors en bas ou dans uen fonction a part

    def result_secret(self):

        pass

    result_secret.__doc__  # idem
    help(result_secret)  # idem

    def evaluation_code(self, code_secret, code_entree):  # ne sert a rien
        """
        Evalution combinaisn
        secret. # ? que voulez vous dire ?
        """
        self.position = (code_secret, code_entree)  # ne veut rien dire.

    def __str__(self):
        return f"code indéfinie de position {self.position}"

    evaluation_code.__doc__a  # idemt
    help(evaluation_code)  #


# if __name__ == '__main__'  ?
def main():
    print("Bienvenue")
    if __name__ == "__main__":
        doctest.testmod()


main()

# doctest hashed values
couleurs = ["bleu", "rose", "or", "argent"]
print("dict:", {x: len(x) for x in couleurs})
print("set :", set(couleurs))

# doctest private tests
__test__ = {
    "numbers": """
>>> evaluation_code('br','br')
[2, 2]

>>> evaluation_code('br','bo')
[1, 1]
""",
    "external": doctest_private_tests_external,
}
# ???? Que voules vous faire

################################################   Tests unitaires ################################################

import unittest

# unittest truth
class jeu(unittest.TestCase):  # TestJeu
    def testAssertTrue(self):
        self.assertTrue(True, " Vous avez gagné le jeu :) ")

    def testAssertFalse(self):
        self.assertFalse(False, " vous avez perdu le jeu :(")


################################################ Autre tests ################################################

# les tests sont automatiques .... ou alors a part mais pas a chaque import du module
# limit dans if __name__ == '__main___':
code_secret = input(" entrer un code secret : ")
pions = input(" entrer des pions : ")
if code_secret == pions:
    print(" mot de passe trouvé ! ")
else:
    print("Vous avez pas trouvé le code secret ! ")


# La fonction shuffle est utilisé pour choisir une couleur aléatoire.
# Non c'est random.choice, shuffle renvoie un liste melangée
liste_couleurs = list(couleurs)
shuffle(liste_couleurs)
print(couleurs, liste_couleurs)

x = 0
for valeur in couleurs:
    if liste_couleurs[x] == valeur:
        print(" pion ", valeur, " à la place ", x)
    else:
        print(" pions à la place ", x)

    x += 1
