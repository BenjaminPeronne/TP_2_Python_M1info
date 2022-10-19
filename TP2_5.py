# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-19 11:22:36
#  * @modify date 2022-10-19 11:22:36
#  * @desc [TP2 - Exercice 5]
#  */


# ================================================

# Un ordinateur n’est qu’un automate programmé fini. Il est sûr que l’on ne peut espérer effectuer des calculs avec une précision infinie, ce qui conduit à des « erreurs d’arrondi ». Quelle précision peut-on espérer ?
# On va définir l’epsilon-machine comme la plus grande valeur ε telle que15: 1+ε = 1
# • Initialiser une variable dx à la valeur 1.0.
# • Dans une boucle while, diviser dx par 2 tant que la condition(1.0 + dx > 1.0)
# est vraie.
# • Afficher la valeur dx finale. Comparer cette valeur avec une valeur normalement nulle(exemple la valeur de sin(π)).

# ================================================

import numpy as np


def main():
    dx = 1.0
    while 1.0 + dx > 1.0:
        dx /= 2
    print(dx)
    print("sin(π) = ", np.sin(np.pi))


if __name__ == '__main__':
    main()
