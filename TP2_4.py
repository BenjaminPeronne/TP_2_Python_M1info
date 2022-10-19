# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-19 11:20:56
#  * @modify date 2022-10-19 11:20:56
#  * @desc [TP2 - Exercice 4]
#  */


# Objectif : Afficher la somme des 10 premiers entiers de trois façons différentes:
# • en utilisant la formule classique:
# • en utilisant une boucle while
# • en utilisant une boucle for.


def main():
    # Formule classique
    print("Formule classique")
    print("=====================================")
    print(sum(range(1, 11)))
    print("===================================== \n")

    # Boucle while
    i = 0
    somme = 0
    while i < 11:
        somme += i
        i += 1
    print("Boucle while")
    print("=====================================")
    print(somme)
    print("===================================== \n")

    # Boucle for
    somme = 0
    for i in range(11):
        somme += i
    print("Boucle for")
    print("=====================================")
    print(somme)
    print("===================================== \n")


if __name__ == '__main__':
    main()
