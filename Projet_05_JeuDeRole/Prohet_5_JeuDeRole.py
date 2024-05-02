###############
# JEU DE ROLE #
###############

"""

Principe du jeu:

- Le jeu comporte deux joueurs: vous et un ennemi
- Vous commencez tous les deux avec 50 points de vie
- Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie
- L'ennemi ne dispose d'aucune potion
- Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50
- Votre attaque inflige à l'ennemi des dégâts aléatoire de points de vie compris entre 5 et 10 points de vie
- L'attaque de l'ennemi vos inflige des dégâts aléatoires compris entre 5 et 10 points de vie
- Lorsque vous utilisez une potion, vous passez le prochain tour

Déroulé de la partie:

- Lorsque vous lancez le script, vous devez demander à l'utilisateur s'il souhaite attaque ou utiliser une potion:
        "Souhaitez-vous attaquer (1) ou utiliser une potion (2)"


"""
import random
import emoji

# Points de vie de départ utilisateur et IA
Pts_Vie_Utilisateur = 50
Pts_Potions_Utilisateur = 3
Pts_Vie_IA = 50

while(True):

    # Saisie utilisateur
    varAction = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? : ")
    if ( (not varAction.isdigit()) or (int(varAction) < 1 and int(varAction) > 2) ):
        continue
    elif varAction == "1":
        # Attaque utilisateur
        varDegats = random.randint(5,10)
        Pts_Vie_IA = Pts_Vie_IA - varDegats
        print(f"Vous evez infligé {varDegats} points de dégats à l'ennemi")
        if Pts_Vie_IA < 1:
            print("Vous avez gagné !")
            print("Fin du jeu.")
            break
        # Attaque IA
        varDegats = random.randint(5,10)
        Pts_Vie_Utilisateur = Pts_Vie_Utilisateur - varDegats
        if Pts_Vie_Utilisateur < 1:
            print("Vous avez perdu !")
            print("Fin du jeu.")
            break
        # Update infos 
        print(f"L'ennemi vous a infligé {varDegats} points de dégats")
        print(f"Il vous reste {Pts_Vie_Utilisateur} points de vie.")
        print(f"Il reste {Pts_Vie_IA} points de vie à l'ennemi.")
        print("--------------------------------------------------------------------")
        continue
    elif varAction == "2":
        if Pts_Potions_Utilisateur > 0:
            Pts_Potions_Utilisateur -= 1
            # Soins de potion
            varSoins = random.randint(15,50)
            Pts_Vie_Utilisateur = Pts_Vie_Utilisateur + varSoins
            # Attaque IA
            varDegats = random.randint(5,10)
            Pts_Vie_Utilisateur = Pts_Vie_Utilisateur - varDegats
            if Pts_Vie_Utilisateur < 1:
                print("Vous avez perdu !")
                print("Fin du jeu.")
                break
            # Update infos
            print(f"Vous récupérez {varSoins} points de vie ({Pts_Potions_Utilisateur}) potions restantes")
            print(f"L'ennemi vous a infligé {varDegats} points de dégats")
            print(f"Il vous reste {Pts_Vie_Utilisateur} points de vie.")
            print(f"Il reste {Pts_Vie_IA} points de vie à l'ennemi.")
            # Utilisateur passe son tour
            print("--------------------------------------------------------------------")
            # Attaque IA
            varDegats = random.randint(5,10)
            Pts_Vie_Utilisateur = Pts_Vie_Utilisateur - varDegats
            if Pts_Vie_Utilisateur < 1:
                print("Vous avez perdu !")
                print("Fin du jeu.")
                break
            # Update infos 
            print(f"L'ennemi vous a infligé {varDegats} points de dégats")
            print(f"Il vous reste {Pts_Vie_Utilisateur} points de vie.")
            print(f"Il reste {Pts_Vie_IA} points de vie à l'ennemi.")
            print("--------------------------------------------------------------------")
            continue
        else:
            print("Vous n'avez plus de potions...")
            continue

