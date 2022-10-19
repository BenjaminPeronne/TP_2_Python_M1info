import names
import random

salle1 = "Salle 1"
spectateurs1 = [names.get_last_name() for i in range(random.randint(5, 20))]

salle2 = "Salle 2"
spectateurs2 = [names.get_last_name() for i in range(random.randint(5, 20))]
spectateurs2.append(spectateurs1[4])


salle3 = "Salle 3"
spectateurs3 = [names.get_last_name() for i in range(random.randint(5, 20))]
spectateurs3.append(spectateurs1[4])

trajet = [(91.68, 53.10), (81.52, 50.14), (43.68, 18.18)]
