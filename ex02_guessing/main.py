import random

petit = input("Entrez la plus petite valeur possible : \n")
grand =  input("Entrez la plus grande valeur possible : \n")
nombre = random.randint(int(petit), int(grand)) 

print ("j'ai pense a un chiffre entre {} et {}".format(petit, grand))

x = 0
while x != nombre:
    x = int(input("Devinez le chiffre:"))
    if x < nombre:
        print("Votre choix est trop petit")
    elif x > nombre:
        print("Votre choix est trop grand")   
    else:
        print("Bravo tu as gagné! Le chiffre était {}".format(nombre))
