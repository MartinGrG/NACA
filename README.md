# Profil NACA symétrique

## Objectif
Ce projet permet d'afficher le profil d'un NACA symétrique chosir par l'utilisateur.

## Requirements
Les librairies numpy et matplolib sont requises

## Fonctionnement
Après avoir lancé le fichier main.py, l'utilisateur doit fournir 4 informations qui lui sont demandées tout à tout:
- Les deux dernier chiffres (XX) du profil sous la NACA00XX choisit
- La longueure de la corde en mètre
- Le nombre de points le long de la corde pour le tracé
- Le type de distribution de points le long de la corde : linéaire ou non-uniforme 

## Contenu
Le projet contient deux 3 fichiers:
- main.py
- profil_aile.py
- README.md

main.py : est le script que doit lancer l'utilisateur pour faire focntionner le code. Il demande à l'utilisateur diverses 
information et affiche le profil d'aile associé.

profil_aile.py: contient la fonction profil_aile qui retourne le tableau des coordonnées des points à afficher en focntion 
de la corde, le nombre de points le long de la corde pour le tracé et l'epaisseur max du profil.