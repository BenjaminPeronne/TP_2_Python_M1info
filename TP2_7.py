# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-19 11:38:10
#  * @modify date 2022-10-19 11:38:10
#  * @desc [TP2 - Exercice 7]
#  */


from enquete_m import *


def main():
    pres12 = []  # liste des spectateurs présents dans les salles 1 et 2
    pres123 = []  # liste des spectateurs présents dans les salles 1, 2 et 3
    for spectateur in spectateurs1:
        pres12.append(spectateur)
    for spectateur in spectateurs2:
        pres12.append(spectateur)

    for spectateur in pres12:
        pres123.append(spectateur)
    for spectateur in spectateurs3:
        pres123.append(spectateur)

    print(set(spectateurs1) & set(spectateurs2) & set(spectateurs3) == set(pres123))
    distances = []

    for i in range(len(trajet)-1):
        distances.append(((trajet[i][0]-trajet[i+1][0])**2+(trajet[i][1]-trajet[i+1][1])**2)**0.5)
    print(distances)
    print("\nLa distance totale est de", sum(distances))

    parcouru = 0
    for i in distances:
        parcouru += i
    # print(parcouru)
    print("\nLa distance totale est de", parcouru)

    for i in range(25, 140, 15):

        print(f"\nPour une vitesse de {i}km/h, il aurait fallu {parcouru/i}h pour parcourir la distance totale")


if __name__ == "__main__":
    main()
