#Fonction vérifiant si l'entrée de l'utilisateur est correcte

def test_input(entree,type):
    if type == 1: #Test pour nom
        #L'entrée doit être 2 chiffres
        if not entree.isdigit():    #Doit être un chiffre
            ans = input("La réponse doit être 2 chiffres: \n")
            return test_input(ans, 1)
        elif len(entree) != 2:      #Doit être de taille 2
            ans = input("La réponse doit être 2 chiffres: \n")
            return test_input(ans, 1)
        else:
            return entree
    if type == 2: #Test corde
        # L'entrée doit être un nombre strictement positif
        if entree.isalpha():    #Test si entree est une lettre
            ans = input("La réponse doit être un nombre strictement positif: \n")
            return test_input(ans, 2)
        elif float(entree) <= 0:        #Doit être strictement positif
            ans = input("La réponse doit être un nombre strictement positif: \n")
            return test_input(ans, 2)
        else:
            return entree
    if type == 3: #Test nombre de points
        #L'entre doit être un entier supérieur à 1 (sinon on ne peut pas tracer de courbe)
        if not entree.isdigit():    #Doit être un chiffre
            ans = input("La réponse doit être un entier supérieur à 1: \n")
            return test_input(ans, 3)
        elif int(entree) <=1:
            ans = input("La réponse doit être un entier supérieur à 1: \n")
            return test_input(ans, 3)
        else:
            return entree
    if type == 4:  # Test réponse l ou nl
        #L'entrée doit être l ou nl
        if entree != 'l' and entree != "nu":
            ans = input("Entrez 'l' pour linéaire ou 'nu' pour non-uniforme: \n")
            return test_input(ans, 4)
        else:
            return entree
