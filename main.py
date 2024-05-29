"""
But du code:
Afficher la courbe d'un profil NACA00XX symétrique
"""

import matplotlib.pyplot as plt
from profil_aile import profil_aile

#Demande d'information à l'utilisateur
nom = input("Quelles sont les chiffres du profil NACAXXXX ? \n")        #Demande des 4 derniers chiffres
eppaisseur = int(nom[-2:])                                              #Stockage des deux derniers
corde = int(input("Quelle est la longueur de la corde en mètre ? \n"))  #Demande de la corde
nb_points = int(input("Donnez le nombre de point le long du tracé: \n"))#demande du nombre de points pour le tracé

coordonnes = profil_aile(corde, nb_points, eppaisseur)  #Appel de la fonction profil_aile qui renvoit le tableau:
                                                        #[[x_down,y_down],[x_up,y_up]]

#Affichage des résultats
plt.plot(coordonnes[0,:,0],coordonnes[0,:,1],label='Intrados')  #Tracé de x_down et y_down
plt.plot(coordonnes[1,:,0],coordonnes[1,:,1],label='Extrados')  #Tracé de x_upet y_up
plt.xlabel('Corde [m]')
plt.ylabel('Épaisseur [m]')
plt.legend()
plt.grid()
plt.title(f"Profil d'aile NACA{nom}")
plt.show()