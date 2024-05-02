################################
# PROJET 4 : LE NOMBRE MYSTERE #
################################

import random

print()
print("*** Le jeu du nombre mystere ***")
print()

essais = 5
nombre_mystere = random.randint(1, 10)

while(True):
    # Affichage nombre essais
    if essais < 1:
        print(f"Desole ! Tu as perdu ! Le nombre mystere etait {nombre_mystere}")
        quit()
    print()
    print(f"Il te reste {essais} essais")
    essais -= 1

    # Saisie du nombre par l'utilisateur
    while(True):
        varIn = input("Devine le nombre entre 1 et 10 : ")
        if not varIn.isdigit():
            print("Veuillez entrer un nombre valide")
            print()
            continue
        if varIn.isdigit():
            break
        
    # Comparaison de la saisie et du nombre mystere
    varIn = int(varIn)
    if varIn > nombre_mystere:
        print(f"Le nombre mystere est plus petit que {varIn}")
        continue
    elif varIn < nombre_mystere:
        print(f"Le nombre mystere est plus grand que {varIn}")
        continue
    elif varIn == nombre_mystere:
        print(f"Bravo tu as trouvé. Le nombre mystere etait bien {varIn}")
        break
