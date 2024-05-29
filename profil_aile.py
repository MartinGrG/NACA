"""
Fonction calculant les coordonnées (x_down,y_down) et (x_up,y_up)
"""

import numpy as np

def profil_aile(corde, nb_points, epaisseur):
    t = epaisseur/100   #Calcul du pourcentage de l'épaisseur maximale
    #Calcul des coordonnées
    #Abscisse
    x_c = np.linspace(0,1,num=nb_points) #Liste x_c debut: 0, fin: longueur corde, pas: corde/nb_points
    x_up = x_c*corde
    x_down = x_up
    #Ordonnée
    y_t = 5*t*(0.2969*np.sqrt(x_c)-0.1260*x_c-0.3516*np.power(x_c,2)+0.2843*np.power(x_c,3)-0.1036*np.power(x_c,4))
    y_up = y_t*corde
    y_down = -y_up

    # Coordonnées pour chaque partie
    coordonnees_down = np.column_stack((x_down, y_down))        #Tableau de la forme colonne 1: x_down et colonne 2: y_down
    coordonnees_up = np.column_stack((x_up, y_up))              #Tableau de la forme colonne 1: x_up et colonne 2: up
    coordonnees = np.array([coordonnees_down, coordonnees_up])  #Tableau de la forme [[x_down, y_down],[x_up, y_up]]
    return coordonnees
