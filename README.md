# Profil NACA symétrique

## Objectif
Ce projet permet d'afficher le profil d'une aile NACA symétrique chosir par l'utilisateur.

## Fonctionnement
Après avoir lancé le fichier main.py, l'utilisateur doit fournir 4 informations qui lui sont demandées tour à tour:
- Les deux dernier chiffres (XX) du profil NACA00XX choisit
- La longueur de la corde en mètre
- Le nombre de points le long de la corde pour le tracé
- Le type de distribution de points le long de la corde : linéaire ou non-uniforme 

## Contenu
Le projet contient 4 fichiers:
- main.py
- profil_aile.py
- test_input.py
- README.md

main.py : est le script que doit lancer l'utilisateur pour faire focntionner le code. Il demande à l'utilisateur diverses 
information et affiche le profil d'aile associé.

profil_aile.py: contient la fonction profil_aile qui retourne le tableau des coordonnées des points pour afficher le profil de l'aile.

test_input.py: contient la fonction qui vérifie si l'entrée de l'utilisateur est correcte 

## Requirements
Les librairies numpy et matplolib sont requises