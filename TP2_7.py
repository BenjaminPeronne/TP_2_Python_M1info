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

    # remplir la liste avec les noms des spectateurs présents dans les salles 1 et 2
    for spectateur in spectateurs1:
        pres12.append(spectateur)
    for spectateur in spectateurs2:
        pres12.append(spectateur)

    # remplir la liste avec les noms des spectateurs présents dans les salles 1, 2 et 3
    for spectateur in spectateurs1:
        pres123.append(spectateur)
    for spectateur in spectateurs2:
        pres123.append(spectateur)
    for spectateur in spectateurs3:
        pres123.append(spectateur)

    # ==================== Tests ====================

    # print("Spectateurs présents dans la salle 1 :")
    # for spectateur in spectateurs1:
    #     print(spectateur)

    # print("\nSpectateurs présents dans la salle 2 :")
    # for spectateur in spectateurs2:
    #     print(spectateur)

    # print("\nSpectateurs présents dans la salle 3 :")
    # for spectateur in spectateurs3:
    #     print(spectateur)

    # print("\nSpectateurs présents dans les deux premiers salles :")
    # for spectateur in pres12:
    #     print(spectateur)

    # Afficher le nombre de spectateurs présents dans les salles 1 et 2
    # print("Nombre de spectateurs présents dans les salles 1 et 2 : " + str(len(pres12)))
    # Afficher le nombre de spectateurs présents dans les salles 1, 2 et 3
    # print("Nombre de spectateurs présents dans les salles 1, 2 et 3 : " + str(len(pres123)))

    # ==================== Tests ====================

    print(set(spectateurs1) & set(spectateurs2) & set(spectateurs3) == set(pres123))
    distances = []

    for i in range(len(trajet)-1):
        # Calcul de la distance entre deux points
        distances.append(((trajet[i][0]-trajet[i+1][0])**2+(trajet[i][1]-trajet[i+1][1])**2)**0.5)
    print(distances)

    parcouru = 0
    for i in distances:
        parcouru += i
    print("\nLa distance totale est de", parcouru)

    for i in range(25, 140, 15):
        print(f"Pour une vitesse de {i}km/h, il aurait fallu {round(parcouru/i, 2)}h pour parcourir la distance totale")


if __name__ == "__main__":
    main()
