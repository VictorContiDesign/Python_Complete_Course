##################################
# PROYECTO 06 : LISTA DE COMPRAS #
##################################

intro = """
Eliga entre las 5 opciones siguientes :

1: Agragar un elemento a la lista
2: Suprimir un elemento de la lista
3: Mostrar la lista
4: Vaciar la lista
5: Salir del programa"""

import os
import json

varChoix = ""
varListe = []

# Recuperamos la lista del fichero json para restaurarla en el script
if os.path.exists("ListeCourses.json"):
    fichierListe = open("ListeCourses.json", "r")
    contenu = json.load(fichierListe)
    fichierListe.close()
    varListe = contenu

while (varChoix != 5):
    # Imprimimos en pantalla las instrucciones a seguir para modificar la lista
    print()
    print(intro)
    print()

    # Eleccion y verificacion de la opcion del usuario
    while(True):
        varChoix = input("Elige una opcion : ")
        print()
        if not varChoix.isdigit():
            print("Indica una cifra de 1 a 5 !")
            print()
            continue
        if varChoix.isdigit():
            varChoix = int(varChoix)
            if(varChoix < 1 or varChoix > 5):
                print("Elige una opcion correcta !")
                print()
                continue
            if(varChoix == 5):
                # Creation d'un fichier json pour stocker
                fichierListe = open("ListeCourses.json", "w")
                json.dump(varListe, fichierListe)
                fichierListe.close()
                print("Hasta luego !")
                exit
            if(varChoix >= 1 or varChoix <= 5):
                break

    # 1. Agregar un elemento a la lista
    if varChoix == 1:
        varAjout = " "
        while(varAjout != ""):
            varAjout = input("Escribe el nombre del elemento que quieres agregar a la lista (ENTER para terminar) : ")
            varAjout = varAjout.upper()
            if varAjout == "":
                continue
            if varAjout in varListe:
                print(f"{varAjout} ya esta en tu lista")
                continue
            # varAjout = varAjout.upper()
            varListe.append(varAjout)
            print(f"{varAjout} ha sido agregado a la lista")

    # 2. Retirar un elemento de la lista
    if varChoix == 2:
        varCancel = input("Escribe el nombre del elemento que quieres borrar de la lista : ")
        varCancel = varCancel.upper()
        if varCancel not in varListe:
            print(f"El elemento {varCancel} no esta presente en la lista")
        if varCancel in varListe:
            varListe.remove(varCancel)
            print(f"{varCancel} ha sido correctamente borrado de la lista")

    # 3. Mostrar la lista en pantalla
    if varChoix == 3:
        if bool(varListe) == False:
            print("*** Tu lista esta vacia ***")
        if bool(varListe) == True:
            print("Este es el contenido de tu lista :")
            print()
            for i,j in enumerate(varListe):
                print(str(i).zfill(2), j)

    # 4. Vaciar la lista
    if varChoix == 4:
        varDelete = ""
        while(varDelete != "o" and varDelete != "n"):
            varDelete = input("Suprimir todo el contenido de la lista ? (s/n) : ")
            if(varDelete != "o" and varDelete != "n"):
                print("Indica una opcion correcta por favor !")
                continue
            if varDelete == "n":
                print("Ningun elemento de la lista fue borrado")
                break
            if varDelete == "o":
                varListe.clear()
                print("Toda la lista ha sido borrada")