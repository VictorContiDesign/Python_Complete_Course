def calculatrice(n1, n2, op):

    n1 = int(input("Entrez un premier nombre : "))
    n2 = int(input("Entrez un deuxième nombre : "))
    op = (input("Indiquez l'operation a effectuer : "))

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