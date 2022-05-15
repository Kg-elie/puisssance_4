#########################################
# groupe BI TD 1
# Elie KANGA
# Sarah Medeneche
# Iram MADANI FOUATIH
# https://github.com/uvsq22101259/puisssance_4
#########################################
# commentaire
"""le code ne fonctionne pas si la grille est de 4*4 car il peut prendre\
    les index de la matrice en commençant par le dernier\
    ce qui fausse les placements"""

#########################################
# importation librairie                 #
#########################################

import tkinter as tk
import random as rd
import tkinter.messagebox as tkm


#########################################
# definitions des constantes            #
#########################################

TAILLE = 600
CASE = 6


#########################################
#  definitions des variables            #
#########################################
mat_case = []
joueur = rd.randint(False, True)
mat_mouvement = []
manche = 0
nbr_piece = 0


#########################################
# definitions des fonctions             #
#########################################

def grillage(n, taille):
    """ cree une grille de n**2 case , contenant les jetons\
        et une matrice n**2 qui contiendra les mouvement de ces jetons """
    global mat_case, mat_mouvement

    if len(mat_case) > 0:
        for i in mat_case:
            canvas.delete(i)
        mat_case = []

    rythme = taille // n
    x = 0
    y = 3
    for i in range(n):
        x = 0
        ligne = []
        for j in range(n):
            ligne.append([canvas.create_oval((x, y), (x+rythme, y+rythme),
                                             fill="grey",
                                             outline="blue", width=2), 0])
            x += rythme
        y += rythme
        mat_case.append(ligne)

    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(0)
        mat_mouvement.append(ligne)


def placage(event):
    """permet aux joueurs de placer les jeton et donne l'effet de gravité"""
    global joueur, manche, nbr_piece
    manche += 1
    j = canvas.find_closest(event.x, event.y)
    colonne = j[0] % CASE - 1
    if colonne == -1:
        colonne = len(mat_case)-1
    if mat_case[0][colonne][-1] != 0:
        joueur = not joueur
        tour()
        return
    if mat_case[-1][colonne][-1] == 0:
        if joueur:
            canvas.itemconfig(mat_case[-1][colonne][0], fill="yellow")
            mat_case[-1][colonne][-1] = 1
        else:
            canvas.itemconfig(mat_case[-1][colonne][0], fill="red")
            mat_case[-1][colonne][-1] = 2
        racine.after_idle(inspection)
        joueur = not joueur
        tour()
        mat_mouvement[-1][colonne] = manche
        return

    else:
        for i in range(CASE):
            if mat_case[i+1][colonne][-1] != 0:
                if joueur:
                    canvas.itemconfig(mat_case[i][colonne][0], fill="yellow")
                    mat_case[i][colonne][-1] = 1
                else:
                    canvas.itemconfig(mat_case[i][colonne][0], fill="red")
                    mat_case[i][colonne][-1] = 2
                racine.after_idle(inspection)
                joueur = not joueur
                tour()
                mat_mouvement[i][colonne] = manche
                return


def inspection():
    """inspecte toute la liste pour savoir si il y a un alignement."""
    global nbr_piece, manche
    for i in range(len(mat_case)):

        for colonne in range(len(mat_case)):
            if mat_case[i][colonne][-1] != 0:

                if i <= len(mat_case)-4 and colonne <= len(mat_case) - 4:
                    if (mat_case[i][colonne][-1] == mat_case[i+1][colonne][-1]
                            == mat_case[i+2][colonne][-1] == mat_case[i+3]
                            [colonne][-1]):
                        print("verticale")
                        racine.after(1500, lambda: racine.quit())
                    elif (mat_case[i][colonne][-1] == mat_case[i][colonne+1]
                            [-1] == mat_case[i][colonne+2][-1] == mat_case[i]
                            [colonne+3][-1]):
                        print("horizontal")
                        racine.after(1500, lambda: racine.quit())
                    if (mat_case[i][colonne][-1] == mat_case[i+1][colonne+1]
                            [-1] == mat_case[i+2][colonne+2][-1] == mat_case
                            [i+3][colonne+3][-1]):
                        print("diagonale", i, colonne, "a")
                        racine.after(1500, lambda: racine.quit())
                        return

                elif i <= len(mat_case)-4 and colonne > len(mat_case) - 4:
                    if (mat_case[i][colonne][-1] == mat_case[i+1][colonne]
                            [-1] == mat_case[i+2][colonne][-1] == mat_case[i+3]
                            [colonne][-1]):
                        print("verticale")
                        racine.after(1500, lambda: racine.quit())
                    elif (mat_case[i][colonne][-1] == mat_case[i][colonne-1]
                            [-1] == mat_case[i][colonne-2][-1] == mat_case[i]
                            [colonne-3][-1]):
                        print("horizontal")
                        racine.after(1500, lambda: racine.quit())
                    elif (mat_case[i][colonne][-1] == mat_case[i+1][colonne-1]
                            [-1] == mat_case[i+2][colonne-2][-1] == mat_case
                            [i+3][colonne-3][-1]):
                        print("diagonale", i, colonne, "b")
                        racine.after(1500, lambda: racine.quit())
                        return

                elif i > len(mat_case)-4 and colonne <= len(mat_case) - 4:
                    if (mat_case[i][colonne][-1] == mat_case[i-1][colonne][-1]
                            == mat_case[i-2][colonne][-1] == mat_case[i-3]
                            [colonne][-1]):
                        print("verticale")
                        racine.after(1500, lambda: racine.quit())
                    elif (mat_case[i][colonne][-1] == mat_case[i][colonne+1]
                            [-1] == mat_case[i][colonne+2][-1] == mat_case[i]
                            [colonne+3][-1]):
                        print("horizontal")
                        racine.after(1500, lambda: racine.quit())
                    if (mat_case[i][colonne][-1] == mat_case[i-1][colonne+1]
                            [-1] == mat_case[i-2][colonne+2][-1] == mat_case
                            [i-3][colonne+3][-1]):
                        print("diagonale", i, colonne, "c")
                        racine.after(1500, lambda: racine.quit())
                        return

                elif i > len(mat_case)-4 and colonne > len(mat_case) - 4:
                    if (mat_case[i][colonne][-1] == mat_case[i-1][colonne]
                            [-1] == mat_case[i-2][colonne][-1] == mat_case[i-3]
                            [colonne][-1]):
                        print("verticale")
                        racine.after(1500, lambda: racine.quit())
                    elif (mat_case[i][colonne][-1] == mat_case[i][colonne-1]
                            [-1] == mat_case[i][colonne-2][-1] == mat_case[i]
                            [colonne-3][-1]):
                        print("horizontal")
                        racine.after(1500, lambda: racine.quit())
                    elif (mat_case[i][colonne][-1] == mat_case[i-1][colonne-1]
                            [-1] == mat_case[i-2][colonne-2][-1] == mat_case
                            [i-3][colonne-3][-1]):
                        print("diagonale", i, colonne, "d")
                        racine.after(1500, lambda: racine.quit())
                        return
    if manche == len(mat_case)**2:
        tkm.showwarning("attention", "vous avez plus de place pour jouer.")
        racine.quit()


def annuler():
    """permet de revenir sur la manche précédente."""
    global manche, joueur
    for i in range(len(mat_mouvement)):
        for j in range(len(mat_mouvement)):
            if mat_mouvement[i][j] == manche:
                mat_case[i][j][-1] = 0
                mat_mouvement[i][j] = 0
                canvas.itemconfig(mat_case[i][j][0], fill="grey")
    manche -= 1
    joueur = not joueur
    tour()


def copie():
    """copie la matrice de la partie dans un fichier text."""
    global text, manche
    if text.get() == "":
        tkm.showwarning("attention", "veiller entré un nom à la sauvegarde.")
        return
    fic = open(text.get()+".txt", "w")
    fic.write(str(len(mat_case)) + "\n")
    fic.write(str(manche) + "\n")
    fic.write(str(joueur) + "\n")
    for i in range(len(mat_case)):
        for j in range(len(mat_case)):
            fic.write(str(mat_case[i][j][0]) + " " + str(mat_case[i][j][1]) +
                      " " + str(mat_mouvement[i][j]) + "\n")
    fic.close()


def recuperation():
    """permet de recuperer une partie sauvegarder et la generer."""
    global mat_case, text, manche, joueur
    if text.get() == "":
        tkm.showwarning("attention", "veiller entré le nom de la sauvegarde.")
        return
    fic = open(text.get()+".txt", "r")
    matrice = fic.readlines()
    ligne = 3
    tale = int(matrice[0])
    manche = int(matrice[1])
    if matrice[2] == "False\n":
        matrice[2] = ""
    joueur = bool(matrice[2])
    print(joueur)
    for i in range(tale):
        for j in range(tale):
            donne = matrice[ligne]
            donne = donne.split()
            mat_case[i][j] = [int(donne[0]), int(donne[1])]
            mat_mouvement[i][j] = int(donne[2])
            ligne += 1
    coloriage()


def coloriage():
    """permet de colorier les canvas avec les informations disponible dans la\
        matrice "mat_case"."""
    for i in range(len(mat_case)):
        for j in range(len(mat_case)):
            if mat_case[i][j][1] == 1:
                canvas.itemconfig(mat_case[i][j][0], fill="yellow")
            elif mat_case[i][j][1] == 2:
                canvas.itemconfig(mat_case[i][j][0], fill="red")
            else:
                canvas.itemconfig(mat_case[i][j][0], fill="grey")
    tour()


def tour():
    """montre quel joueur joue"""
    if joueur:
        tour_joueur.config(bg="yellow")
    else:
        tour_joueur.config(bg="red")


#########################################
# programme principal                   #
#########################################

racine = tk.Tk()
racine.title(" PUISSANCE 4")

canvas = tk.Canvas(racine, width=TAILLE, height=TAILLE, bg="blue")
canvas.grid(column=0, row=0, columnspan=3)

canvas.bind("<Button-1>", placage)

retour = tk.Button(racine, text="retour", command=annuler)
retour.grid()

sauvegarde = tk.Button(racine, text="sauvegarder", command=copie)
sauvegarde.grid()

charger = tk.Button(racine, text="charger", command=recuperation)
charger.grid()

text = tk.StringVar()
barre = tk.Entry(racine, textvariable=text, bd=3)
barre.grid()

tour_joueur = tk.Canvas(racine, width=70, height=40, bg="black")
tour_joueur_texte = tour_joueur.create_text(35, 20, text="joueur", font=("\
    courier"), fill="black")
tour_joueur.grid(column=1, row=1)
tour()
titre_jeu = tk.Canvas(racine, width=140, height=40, bg="grey")
titre_jeu_texte = titre_jeu.create_text(70, 20, text="Puissance 4", font=("\
    courier"), fill="black")
titre_jeu.grid(column=2, row=1)
grillage(CASE, TAILLE)
racine.mainloop()
