#########################################
# groupe BI TD 1
# Elie KANGA
# Sarah Medeneche
# Iram MADANI FOUATIH
# https://github.com/uvsq22101259/puisssance_4
#########################################


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
joueur = rd.randint(False,True)
mat_mouvement = []
manche = 0



#########################################
# definitions des fonctions             #
#########################################

def grillage(n,taille):
    """ cree une grille de n^2 case, et donne a chaque case une couleur selectionner en fonction du grain de sable qu'elle contient """
    global mat_case,mat_mouvement
    
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
            ligne.append([canvas.create_oval((x,y),(x+rythme,y+rythme), fill="grey" ,outline="blue", width= 2 ),0])
            x += rythme
        y += rythme
        mat_case.append(ligne)

    for i in range (n):
        ligne = []
        for j in range(n):
            ligne.append(0)
        mat_mouvement.append(ligne)
            
        
    



def placage(event):
    """permet a l'utilisateur de donner des grains de sable lui-meme"""
    global joueur, manche
    manche += 1
    j = canvas.find_closest( event.x, event.y)
    colonne = j[0] % CASE -1
    if colonne == -1:
        colonne = len(mat_case)-1
    if mat_case[0][colonne][-1] != 0:
        joueur = not joueur
        return
    if  mat_case[-1][colonne][-1] == 0:
        if joueur:
            canvas.itemconfig(mat_case[-1][colonne][0], fill ="yellow")
            mat_case[-1][colonne][-1] = 1
        else:
            canvas.itemconfig(mat_case[-1][colonne][0], fill ="red")
            mat_case[-1][colonne][-1] = 2
        inspection()
        joueur = not joueur
        mat_mouvement[-1][colonne] = manche
        return
        
    else:
        for i in range(CASE):
            if mat_case[i+1][colonne][-1] != 0:
                if joueur:
                    canvas.itemconfig(mat_case[i][colonne][0], fill ="yellow")
                    mat_case[i][colonne][-1] = 1
                else:
                    canvas.itemconfig(mat_case[i][colonne][0], fill ="red")
                    mat_case[i][colonne][-1] = 2
                inspection()
                joueur = not joueur
                mat_mouvement[i][colonne] = manche
                return


def inspection():
    
    for i in range (len(mat_case)):

        for colonne in range(len(mat_case)):
            if mat_case[i][colonne][-1] != 0:
                if i <= len(mat_case)-4 and colonne <= len(mat_case)-4 :
                    if   mat_case[i][colonne][-1] == mat_case[i+1][colonne][-1] == mat_case[i+2][colonne][-1] == mat_case[i+3][colonne][-1]:
                        print("victoire verticale",colonne)
                    elif mat_case[i][colonne][-1] == mat_case[i][colonne+1][-1] == mat_case[i][colonne+2][-1] == mat_case[i][colonne+3][-1]:
                        print("victoire horizontale",i)
                    if mat_case[i][colonne][-1] == mat_case[i+1][colonne+1][-1] == mat_case[i+2][colonne+2][-1] == mat_case[i+3][colonne+3][-1]:
                        print("victoire diagonale",colonne,i)
                        return
                    

                elif i <= len(mat_case)-4 and colonne > len(mat_case)-4 :
                    if   mat_case[i][colonne][-1] == mat_case[i+1][colonne][-1] == mat_case[i+2][colonne][-1] == mat_case[i+3][colonne][-1]:
                        print("victoire verticale",colonne)
                    elif mat_case[i][colonne][-1] == mat_case[i][colonne-1][-1] == mat_case[i][colonne-2][-1] == mat_case[i][colonne-3][-1]:
                        print("victoire horizontale",i)
                    elif mat_case[i][colonne][-1] == mat_case[i+1][colonne-1][-1] == mat_case[i+2][colonne-2][-1] == mat_case[i+3][colonne-3][-1]:
                        print("victoire diagonale",colonne,i)
                        return

                elif i > len(mat_case)-4 and colonne <= len(mat_case)-4 :
                    if   mat_case[i][colonne][-1] == mat_case[i-1][colonne][-1] == mat_case[i-2][colonne][-1] == mat_case[i-3][colonne][-1]:
                        print("victoire verticale",colonne)
                    elif mat_case[i][colonne][-1] == mat_case[i][colonne+1][-1] == mat_case[i][colonne+2][-1] == mat_case[i][colonne+3][-1]:
                        print("victoire horizontale",i)
                    if mat_case[i][colonne][-1] == mat_case[i-1][colonne+1][-1] == mat_case[i-2][colonne+2][-1] == mat_case[i-3][colonne+3][-1]:
                        print("victoire diagonale",colonne,i)
                        return

                elif i > len(mat_case)-4 and colonne > len(mat_case)-4 :
                    if   mat_case[i][colonne][-1] == mat_case[i-1][colonne][-1] == mat_case[i-2][colonne][-1] == mat_case[i-3][colonne][-1]:
                        print("victoire verticale",colonne)
                    elif mat_case[i][colonne][-1] == mat_case[i][colonne-1][-1] == mat_case[i][colonne-2][-1] == mat_case[i][colonne-3][-1]:
                        print("victoire horizontale",i)
                    elif mat_case[i][colonne][-1] == mat_case[i-1][colonne-1][-1] == mat_case[i-2][colonne-2][-1] == mat_case[i-3][colonne-3][-1]:
                        print("victoire diagonale",colonne,i)
                        return



def annuler():
    global manche, joueur
    for i in range(len(mat_mouvement)):
        for j in range(len(mat_mouvement)):
            if  mat_mouvement[i][j] == manche:
                mat_case[i][j][-1] = 0
                mat_mouvement[i][j] = 0
                canvas.itemconfig(mat_case[i][j][0], fill ="grey")
    manche -= 1
    joueur = not joueur




def copie():
    """copie la matrice d'une configuration dans un fichier text"""
    global text
 
    

def recuperation():
    """permet de recuperer une configuration sauvegarder et la generer"""
    global mat_case, text
    




#########################################
# programme principal                   #
#########################################


racine = tk.Tk()
racine.title(" PUISSANCE 4")
canvas = tk.Canvas(racine,width= TAILLE, height= TAILLE, bg= "blue")
canvas.grid(column=0,row=0, rowspan= 20)
canvas.bind("<Button-1>",placage)
retour = tk.Button(racine,text="retour",command=annuler)
retour.grid()
sauvegarde = tk.Button(racine, text="sauvegarder",command= copie)
sauvegarde.grid()
charger = tk.Button(racine,text="charger", command = recuperation)
charger.grid()
text = tk.StringVar()
barre = tk.Entry(racine,textvariable= text, bd= 3)
barre.grid()
grillage(CASE,TAILLE)
racine.mainloop()
print(mat_case)