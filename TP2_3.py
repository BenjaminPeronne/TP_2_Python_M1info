# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-19 11:14:37
#  * @modify date 2022-10-19 11:14:37
#  * @desc [TP2 - Exercice 3]
#  */


# objectif : Vous jouez avec deux dés et vous voulez savoir combien il y a de façons de faire un certain nombre. Bien noter qu’il y a deux façons d’obtenir 3: 1-2 et 2-1.


def main():
    nombre = int(input("Entrez un nombre entre 2 et 12 : "))
    if nombre < 2 or nombre > 12:
        print("Le nombre doit être compris entre 2 et 12")
        return
    compteur = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == nombre:
                compteur += 1
    print(f"Il y a {compteur} possibilités pour faire {nombre}")


if __name__ == '__main__':
    main()
