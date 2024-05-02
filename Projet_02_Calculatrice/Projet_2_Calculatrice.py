#################################
### PROJET n°2 : CALCULATRICE ###
#################################

n1 = ''
n2 = ''
op = ''

############
# FUNCTIONS

def calculatrice(n1, n2, op):

    # On verifie que les saisies des operateurs soient bien des valeurs numeriques
    while(True):
        if not str(n1).isdigit():
            try:
                n1 = int(input("Entrez un premier nombre : "))
            except:
                print("Veuillez entrer une valeur numérique !")
                continue
        if not str(n2).isdigit():
            try:
                n2 = int(input("Entrez un deuxième nombre : "))
            except:
                print("Veuillez entrer une valeur numérique !")
                continue
        if str(n1).isdigit() and str(n2).isdigit():
            break

    # On verifie que la saisie de l'operation soit bien le symbole d'une operation mathematique
    while((op != "+") and (op != "+") and (op != "+") and (op != "+")):
        op = (input("Indiquez l'operation a effectuer : "))
        if ((op == "+") or (op == "*") or (op == "/") or (op == "%")):
            break
        else:
            print("Veuillez indiquer une operation mathematique correcte !")
            continue

    # On fait l'operation mathematique en fonction du symbole qui a ete saisie
    if(op == "+"):
        print(f"Le résultat de l'addition de {n1} avec {n2} est égal à {n1 + n2}")
    elif(op == "*"):
        print(f"Le résultat de la multiplication de {n1} avec {n2} est égal à {n1 * n2}")
    elif(op == "/"):
        print(f"Le résultat de la division de {n1} avec {n2} est égal à {n1 / n2}")
    elif(op == "%"):
        print(f"Le résultat du modulo de {n1} avec {n2} est égal à {n1 % n2}")
    else:
        print("Indiquez l'operation a effectuer : ")


###############
# MAIN PROGRAM

print()
print("/********************/")
print("/*** CALCULATRICE ***/")
print("/********************/")
print()
question = input("Voulez-vous faire un calcul ? (o/n) : ").lower()
if(question != "o"):
    exit

while(question == "o"):
    calculatrice(n1, n2, op)
    question = input("Voulez-vous faire un autre calcul ? (o/n) : ").lower()
    print()
    if(question != "o"):
        exit


