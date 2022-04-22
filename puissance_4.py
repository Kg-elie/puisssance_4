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
from unittest import case



#########################################
# definitions des constantes            #
#########################################

TAILLE = 600
CASE = 6


#########################################
#  definitions des variables            #
#########################################
mat_case = []



#########################################
# definitions des fonctions             #
#########################################

def grillage(n,taille):
    """ cree une grille de n^2 case, et donne a chaque case une couleur selectionner en fonction du grain de sable qu'elle contient """
    global mat_case
    
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

    # for i in range (n):
    #     x = 3
    #     for j in range(n):
    #         mat_case.append(canvas.create_oval((x,y),(x+rythme,y+rythme), fill="grey" ,outline="blue", width= 2 ))
    #         x += rythme
        
    



def placage(event):
    """permet a l'utilisateur de donner des grains de sable lui-meme"""
    j = canvas.find_closest( event.x, event.y)
    colonne = j[0] % CASE -1
    # print('lignes',colonne)
    if  mat_case[-1][colonne][-1] == 0:
        canvas.itemconfig(mat_case[-1][colonne][0], fill ="yellow")
        mat_case[-1][colonne][-1] = 1
    else:
        for i in range(CASE):
            if mat_case[i+1][colonne][-1] == 1:
                canvas.itemconfig(mat_case[i][colonne][0], fill ="yellow")
                mat_case[i][colonne][-1] = 1
                return


def victoire():

    for i in range(CASE):
        for j in range(CASE):
            if i 

            

    
    
        







#########################################
# programme principal                   #
#########################################


racine = tk.Tk()
racine.title(" PUISSANCE 4")
canvas = tk.Canvas(racine,width= TAILLE, height= TAILLE, bg= "blue")
canvas.grid(column=0,row=0, rowspan= 20)
canvas.bind("<Button-1>",placage)
grillage(CASE,TAILLE)
racine.mainloop()