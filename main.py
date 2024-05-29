import matplotlib.pyplot as plt
from profil_aile import profil_aile

#Demande d'information à l'utilisateur
nom = input("Quelles sont les chiffres du profil NACAXXXX ? \n")
eppaisseur = int(nom[-2:])
corde = int(input("Quelle est la longueur de la corde en mètre ? \n"))
nb_points = int(input("Donnez le nombre de point le long du tracé: \n"))

coordonnes = profil_aile(corde, nb_points, eppaisseur)

#Affichage des résultats
plt.plot(coordonnes[0,:,0],coordonnes[0,:,1],label='Intrados')
plt.plot(coordonnes[1,:,0],coordonnes[1,:,1],label='Extrados')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title(f"Profil d'aile NACA{nom}")
plt.show()