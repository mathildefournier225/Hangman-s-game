

def afficherPendu(lettresIncorrectes):
    listforme=[" ","==="," | \n | \n | \n===","+---+ \n    | \n    | \n    | \n   ===","+---+ \nO   | \n    | \n    | \n   ===","+---+ \nO   | \n|   | \n    | \n   ==="," +---+ \n O   | \n-|   | \n     | \n    ==="," +---+ \n O   | \n-|-  | \n     | \n    ==="," +---+ \n O   | \n-|-  | \n/    | \n    ==="," +---+ \n O   | \n-|-  | \n/ \  | \n    ==="]
    v=listforme[len(lettresIncorrectes)]#pour afficher le dessin du pendu qui correspond au nombre d'erreurs
    return v


def choisirMot():
    try:#je rajoute le try  ici pour fermer à la fin le fichier même si il y a des exceptions
        mots=open("mots.txt")
        liste=mots.readlines()#pour lire les mots et les ajouter dans la liste 
        liste_mots=[]
        mots.close()
        for i in range(len(liste)): #stocker les mots ayant au moins 3lettres
            if len(liste[i])>3:
                liste_mots.append(liste[i])
        from random import randint
        mot=liste_mots[randint(0,len(liste_mots))]#pour prendre un mot au hazard dans la liste
    finally:
        mots.close()
    return mot


def getLettre():
    lettre=input("saisir lettre: ")
    while lettre.isalpha()==False : #tant que ce que l'utilisateur ne saisi pas de lettre
        lettre=input("saisir lettre: ")
    
    lettre=lettre.lower()#pour mettre la lettre en minuscule
    return lettre


def verifLettre(lettre,mot,lettresIncorrectes,lettresCorrectes):
    Lettre=False #création du bouléen pour renvoyer si oui ou non la lettre est dans le mot
    for i in range (len(mot)):
        if mot[i]==lettre:
            lettresCorrectes[i]=lettre
            Lettre=True #lettre devient true et comme ca la lettre ne sera pas ajoutée à la liste des lettres incorrectes
    if lettre not in lettresIncorrectes:#on verifie si la lettres n'est pas deja dans les lettres incorrectes pour ne pas compter plusieurs erreurs
        if Lettre==False:
            lettresIncorrectes.append(lettre)
    
    print("mot:",lettresCorrectes)
    print("lettres incorrectes:",lettresIncorrectes) 
    

def jouerPendu():
    #initialisation des variables
    mot=choisirMot()
    lettresIncorrectes=[]
    lettresCorrectes=[]
    for i in range (len(mot)-1):#dans mon fichier mot je suis retourné à la ligne après les mots, il compte dons un caractere en plus donc je mets len(mot)-1
        lettresCorrectes.append("_")#pour écrire le mot avec les traits et qu'il y ait le même nombre de traits que de lettres
    
    print("mot:",lettresCorrectes)
    print("lettres incorrectes:",lettresIncorrectes)
    
    #jeu
    victoire=True #je crée ce bouléen pour permettre d'afficher ou non le petit message de victoire à la fin
    while "_" in lettresCorrectes: #pour continuer le jeu tant que toutes les lettres ne sont pas trouvées
        lettre=getLettre()#on appelle ici la fonction getLettre pour que l'utilisateur saisisse une lettre
        
        #cette partie permet à l'utilisateur de pouvoir saisir le mot en entier s'il l'a trouver sans faire lettre par lettre
        if len(lettre)>1:
            if (lettre+"\n")==mot:#je rajoute ici \n apres lettre car tous les mots sont entrés avec un retour à la ligne apres eux dans mon fichier mot
                break
            print("Ce n'est pas le bon mot")
        else:
            verifLettre(lettre,mot,lettresIncorrectes,lettresCorrectes)#on verifie si la lettre est dans le mot
            print(afficherPendu(lettresIncorrectes))
        
            
        if afficherPendu(lettresIncorrectes)==" +---+ \n O   | \n-|-  | \n/ \  | \n    ===": #si le dernier schéma du pendu s'affiche la partie est finie
            print("vous avez perdu! le mot était:",mot)
            victoire=False
            break #pour arrêter la boucle while si jamais le joueur a perdu
    if victoire==True:
        print("bravo vous avez gagné! Le mot était : ",mot)
        
jouerPendu()