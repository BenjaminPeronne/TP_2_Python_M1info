# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-19 11:28:56
#  * @modify date 2022-10-19 11:28:56
#  * @desc [TP2 - Exercice 6]
#  */

def main():
    coords = [(4, 5), (9, 3), (12, 8), (13, 7), (18, 6), (20, 9)]
    ordos = []

    # remplir la liste d'ordonnées en parcourant la liste des coordonnées
    for coord in coords:
        ordos.append(coord[1])
    print(ordos)

    # filtrer le contenu de coords afin de borner à 7 toutes les ordonnées qui y sont supérieure
    for i in range(len(coords)):
        if coords[i][1] > 7:
            coords[i] = (coords[i][0], 7)

    print("\ncoords après traitement :")
    print(coords)


if __name__ == '__main__':
    main()
