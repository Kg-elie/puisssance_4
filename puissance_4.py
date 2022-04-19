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
case_id = []



#########################################
# definitions des fonctions             #
#########################################

def grillage(n,taille):
    """ cree une grille de n^2 case, et donne a chaque case une couleur selectionner en fonction du grain de sable qu'elle contient """
    global case_id
    
    if len(case_id) > 0:
        for i in case_id:
            canvas.delete(i)
        case_id = []
    
    rythme = taille // n
    x = 0
    y = 3
    
    for i in range (n):
        x = 3
        for j in range(n):
            case_id.append(canvas.create_oval((x,y),(x+rythme,y+rythme), fill="grey" ,outline="blue", width= 2 ))
            x += rythme
        y += rythme

def mode_player(event):
    """permet a l'utilisateur de donner des grains de sable lui-meme"""
    j = canvas.find_closest( event.x, event.y)
    # print(j[0])
    canvas.itemconfig(j[0], fill ="yellow")

    
        
        
    






#########################################
# programme principal                   #
#########################################


racine = tk.Tk()
racine.title("TAS DE SABLE")
canvas = tk.Canvas(racine,width= TAILLE, height= TAILLE, bg= "blue")
canvas.grid(column=0,row=0, rowspan= 20)
canvas.bind("<Button-1>",mode_player)
grillage(CASE,TAILLE)
racine.mainloop()