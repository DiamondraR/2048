import random
#creer un tableau temporaire 4 lignes, 4 colonnes avec des listes de liste
#creer des fonctions pour aller vers la gauche, la droite, le haut et le bas
#creer une fonction qui ajoute 2 nombres random dans le tableau au tout début
#creer une fonction pour sommer deux cases 

#tableau temporaire
tab = [[0,2,0,0], [0,2,2,0], [0,4,0,0], [0,4,0,2]]

#la taille du tableau
tabSize = 4

def initialise_tab(size):
    tabSize= size
    tab = []
    for i in range(tabSize):
        tab.append(tabSize * [0])
    nombre = 0
    while (nombre != int(tabSize/2)):
        x = random.randint(0,tabSize -1)
        y = random.randint(0,tabSize -1)
        if tab[x][y] == 0:
            nombre_debut = random.randint(0,100)
            if nombre_debut <= 75:
                tab[x][y] = 2
            else:
                tab[x][y] = 4
            nombre += 1
    return tab




#fonction affichage
def affichage():
    plus_grand_nombre = tab[0][0]
    for ligne in tab:
        for nombre in ligne:
            if nombre > plus_grand_nombre:
                plus_grand_nombre = nombre
    largeur_espace = len(str(plus_grand_nombre))

    for ligne in tab:
        ligneCourant = "|"
        for nombre in ligne:
            if nombre == 0:
                ligneCourant += " " * largeur_espace + "|"
            else:
                ligneCourant += (" " * (largeur_espace - len(str(nombre)))) + str(nombre) + "|"
        print(ligneCourant)
    print()


#fonction pour se déplacer vers la gauche et de sommer 
def somme_ligne_gauche(ligne):
    #pour déterminer la case la plus vers la gauche
    for j in range(tabSize -1):
        for i in range(tabSize -1, 0, -1):
            if (ligne[i - 1] == 0):
                 ligne[i - 1] = ligne[i]
                 ligne[i] = 0
#tout deplacer vers la gauche
    for i in range(tabSize - 1):
        if ligne[i] == ligne[i + 1]:
            ligne[i] *= 2
            ligne[i + 1] = 0
    for i in range (tabSize -1, 0, -1):
        if ligne[i - 1] == 0:
            ligne[i -1] = ligne[i]
            ligne[i] = 0
    return ligne

def somme_tab_gauche(tabCourant):
    for i in range(tabSize):
        tabCourant[i] = somme_ligne_gauche(tabCourant[i])
    return tabCourant  

#tout deplacer vers la droite
def inverser_ligne(ligne):
    ligne_deux = []
    for i in range(tabSize -1):
        ligne_deux[i] = ligne[tabSize -1 -i]
    return ligne_deux

def somme_tab_droite(tabCourant):
    for i in range(tabSize):
        tabCourant[i]= inverser_ligne(somme_ligne_gauche(tabCourant[i]))
    return tabCourant  

#deplacement bas
def somme_ligne_haut(tab, x):
    for j in range(tabSize -1):
        for i in range(tabSize -1, 0, -1):
            if (tab[i - 1][x] == 0):
                 tab[i - 1][x] = tab[i][x]
                 tab[i][x] = 0
#tout deplacer vers le haut
    for i in range(tabSize - 1):
        if tab[i][x] == tab[i + 1][x]:
            tab[i][x] *= 2
            tab[i + 1][x] = 0
    for i in range (tabSize -1, 0, -1):
        if tab[i - 1][x] == 0:
            tab[i -1][x] = tab[i][x]
            tab[i][x] = 0
    return tab

def somme_tab_haut(tabCourant):
    for i in range(tabSize):
        tabCourant=somme_ligne_haut(tabCourant, i)
    return tabCourant

#tout deplacer vers le bas    
def inverser_colonne(tab, x):
    for i in range(int(tabSize/ 2)):
        tampon = tab[i][x]
        tab[i][x] = tab[(tabSize -1 -i)][x]
        tab[(tabSize -1 -i)][x] = tampon
    return tab

def somme_tab_bas(tabCourant):
    for i in range(tabSize):
        tabCourant = inverser_colonne(somme_ligne_haut(tabCourant, i), i)
    return tabCourant    


def rajout_nombre(tabCourant):
    nombre = 0
    while (nombre != 1):
        x = random.randint(0,tabSize -1)
        y = random.randint(0,tabSize -1)
        if tabCourant[x][y] == 0:
            nombre_debut = random.randint(0,100)
            if nombre_debut <= 75:
                tabCourant[x][y] = 2
            else:
                tabCourant[x][y] = 4
            nombre += 1
    return tabCourant

def jeu_fini(tabCourant):
    cpt = 0
    for ligne in tabCourant:
        for valeur in ligne:
            if valeur == 2048 :
                return 0 
            if valeur == 0:
                cpt += 1
    if cpt != 0:
        return 1    
    for i in range(tabSize -1):
        for j in range(tabSize -1):       








    



#somme_tab_gauche(tab)
#somme_tab_droite(tab)
#somme_tab_haut(tab)
#somme_tab_gauche(tab)
tab = initialise_tab(4)
affichage()
somme_tab_gauche(tab)
affichage()
rajout_nombre(tab)

affichage()

