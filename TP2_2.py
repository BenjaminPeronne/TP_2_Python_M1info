# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-19 11:11:57
#  * @modify date 2022-10-19 11:11:57
#  * @desc [TP2 - Exercice 2]
#  */


# Objectif : Tracer, à l’aide d’une boucle while (puis, dans un second temps, à l’aide d’une boucle for), un octogone de 50 pixels de côté .

from turtle import*  # Importation du module turtle


def whileMain():  # Version avec while
    i = 0
    while i < 8:
        forward(50)
        left(45)
        i += 1


def main():  # Version avec for
    for i in range(8):
        forward(50)
        left(45)


if __name__ == '__main__':
    whileMain()
    input("Appuyez sur Entrée pour la suite")
    reset()
    main()
    print("Fin du programme")
