from getpass import getpass

mot = getpass("Entrez votre mot")

liste=[]
votre_liste=[]

for x in mot :
    liste.append(x)
    votre_liste.append('*')

print("".join(votre_liste))   

nb_erreur = 0 
while nb_erreur < 9 :
    lettre = input("Entrez votre lettre")

    if len(lettre)>1:
        if lettre ==mot:
            print("vous avez trouvé")
            break

    if lettre in liste:
        for(index,y) in enumerate(liste):
            if x==lettre:
                votre_liste[index] = x
        v = "".join(votre_liste)
        print("bonne lettre",v)

    else :
        nb_erreur +=1
        print('Mauvaise lettre; il vous reste %s essai'%(9-nb_erreur))
         


