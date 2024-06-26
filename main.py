"""
Le but est d'afficher la courbe d'un profil NACA00XX symétrique
"""

import matplotlib.pyplot as plt
import numpy as np
from profil_aile import profil_aile
from test_input import test_input

#Demande d'information à l'utilisateur
nom = test_input(input("Quelles sont les deux dernier chiffres du profil NACA00XX ? \n"), 1)  #Demande des 4 derniers chiffres
eppaisseur = int(nom)                                                          #Transformation en int
corde = float(test_input(input("Quelle est la longueur de la corde en mètre ? \n"), 2))         #Demande de la corde
nb_points = int(test_input(input("Donnez le nombre de point le long du tracé: \n"), 3))       #Demande du nombre de points pour le tracé
type = test_input(input("Donnez le style de distribution linéaire ou non-uniforme: l ou nu  \n"), 4) #Demande du style de distribution


coordonnes = profil_aile(corde, nb_points, eppaisseur,type)  #Appel de la fonction profil_aile qui renvoit le tableau:
                                                             #[[x_down,y_down],[x_up,y_up]]
#Affichage des résultats
plt.plot(coordonnes[0,:,0],coordonnes[0,:,1],label='Intrados')  #Tracé de x_down et y_down
plt.plot(coordonnes[1,:,0],coordonnes[1,:,1],label='Extrados')  #Tracé de x_upet y_up
plt.xlabel('Corde [m]')                 #Ajout nom de l'abscisse
plt.ylabel('Épaisseur [m]')             #Ajout nom de l'ordonnée

#Choix de la taille des axes pour avoir un tracé centré et avec une proportion
plt.xlim(-corde/2, corde + corde/2)
plt.ylim(np.min(coordonnes[0][:,1])*6, np.max(coordonnes[1][:,1]*6))

plt.legend()                            #Ajout d'une légende
plt.grid()                              #Ajout d'une grille en fond
plt.title(f"Profil d'aile NACA00{nom}") #Ajout du titre
plt.show()                              #Affichage du graph

