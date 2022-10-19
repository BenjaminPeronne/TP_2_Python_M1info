# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-19 11:07:42
#  * @modify date 2022-10-19 11:07:42
#  * @desc [TP2 - Exercice 1]
#  */

# Objectif : Afficher les 20 premiers termes de la table de multiplication par 7, en signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de 3.

# Le programme répond à l'objectif

# ================================================
# ============== Programme principal =============
# ================================================
def main():
    for i in range(20):
        print(i * 7, end=" ")
        if i % 3 == 0:
            print("*", end=" ")
        print()


# ================================================
# ============== Appel au programme principal ====
# ================================================
if __name__ == '__main__':
    main()
