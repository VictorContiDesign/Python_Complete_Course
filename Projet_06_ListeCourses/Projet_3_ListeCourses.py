################################
# PROJET 03 : LISTE DE COURSES #
################################

intro = """
Choisissez parmi les 5 options suivantes:

1: Ajouter un element a la liste
2: Retirer un element a la liste
3: Afficher la liste
4: Vider la liste
5: Quitter"""

import os
import json

varChoix = ""
varListe = []

# Recuperation de la liste du fichier json pour la restaurer dans le script
if os.path.exists("ListeCourses.json"):
    fichierListe = open("ListeCourses.json", "r")
    contenu = json.load(fichierListe)
    fichierListe.close()
    varListe = contenu

while (varChoix != 5):
    # Affichage de consigne
    print()
    print(intro)
    print()

    # Saisie et verification saisie utilisateur
    while(True):
        varChoix = input("Votre choix : ")
        print()
        if not varChoix.isdigit():
            print("Veuillez indiquer un chiffre de 1 a 5 !")
            print()
            continue
        if varChoix.isdigit():
            varChoix = int(varChoix)
            if(varChoix < 1 or varChoix > 5):
                print("Veuillez choisir une option correcte !")
                print()
                continue
            if(varChoix == 5):
                # Creation d'un fichier json pour stocker
                fichierListe = open("ListeCourses.json", "w")
                json.dump(varListe, fichierListe)
                fichierListe.close()
                print("A bientot !")
                exit
            if(varChoix >= 1 or varChoix <= 5):
                break

    # 1. Ajout d'un element a la liste
    if varChoix == 1:
        varAjout = input("Entrez le nom de l'element a ajouter a la liste de courses : ")
        varAjout = varAjout.upper()
        varListe.append(varAjout)
        print(f"{varAjout} a bien ete ajoute a la liste")

    # 2. Retirer un element a la liste
    if varChoix == 2:
        varCancel = input("Entrez le nom de l'element a effacer de la liste de courses : ")
        varCancel = varCancel.upper()
        if varCancel not in varListe:
            print(f"l'Element {varCancel} n'est pas present dans la liste")
        if varCancel in varListe:
            varListe.remove(varCancel)
            print(f"{varCancel} a bien ete efface de la liste")

    # 3. Afficher la liste
    if varChoix == 3:
        if bool(varListe) == False:
            print("*** Votre liste est vide ***")
        if bool(varListe) == True:
            print("Voici le contenu de votre liste :")
            print()
            for i,j in enumerate(varListe):
                print(str(i).zfill(2), j)

    # 4. Vider la liste
    if varChoix == 4:
        varDelete = ""
        while(varDelete != "o" and varDelete != "n"):
            varDelete = input("Supprimer tout le contenu de la liste ? (o/n) : ")
            if(varDelete != "o" and varDelete != "n"):
                print("Veuillez indiquer un choix correct !")
                continue
            if varDelete == "n":
                print("Aucun element de la liste n'a ete efface")
                break
            if varDelete == "o":
                varListe.clear()
                print("Toute la liste a ete efface")