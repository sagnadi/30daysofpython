# Jour2: 30 Days of Python Programming

# ############ Exercice 1 ############ #
prenom = "Maxime" 
nom_de_famille = "ALEDI"
nom_complet = "ALEDI Sagnadi Maxime"
pays  = "TOGO"
municipale = "Nyeve"
an = 32
est_Married = True
is_true = True
IS_light = False
jour, mois, annee = 24, "Juillet", 2025



# ############ Exercice 2 ############ #

# 1 Verification des types de données 
print(type(prenom))
print(type(nom_de_famille))
print(type(nom_complet))
print(type(pays))
print(type(municipale))
print(type(an))
print(type(est_Married))
print(type(is_true))
print(type(IS_light))
print(type(jour))
print(type(mois))
print(type(annee))

# 2 Longueur du prenom
print(len(prenom))

# 3 comparaison des longueurs 
longueur_prenom = len(prenom)
longueur_nom = len(nom_de_famille)
if(longueur_nom==longueur_prenom):
    print("Les deux ont la memme longueur")
elif(longueur_nom>longueur_prenom):
     print("Le nom de famille est plus long que le prenom")
else:
     print("Le prenom est plus long que le nom de famille")

# 4 Declaration 
num_one = 5
num_two = 4

# 5 Addition 
somme = num_one + num_two
print(somme)

# 6 Soustraction
difference = num_one - num_two
print(difference)

# 7 Multiplication
produit = num_one * num_two
print(produit)

# 8 Division
division = num_one / num_two
print(division)

# 9 Module
modulo = num_two % num_one
print(modulo)

# 10 Floor division
floor = num_one // num_two
print(floor)

# 12 calcul de l'air et de la circonference
rayon = 30

# calul de l'air grace à la formule A = pi x r^2 et pi = 3.14
area_of_circle = 3.14 * 30**2
print(area_of_circle)

# cacul de la ciconference grace à la formule C = 2 x pi x r et pi = 3.14
circum_of_circle = 2 * 3.14 * 30
print(circum_of_circle)

# calcule de l'air avec le rayon en entrée utilisateur
rayon_utilisateur = int(input("Entrez le rayon de votre cercle : "))
air_du_cercle = 3.14 * rayon_utilisateur**2
print(air_du_cercle)

# 13 stockage des informations 
prenom_utilisateur = input("Entrez votre prenom: ") # demande le prenom de l'utilisateur
print("Votre prenom est: ", prenom_utilisateur) # affichage du prenom de l'utilisateur

nom_utilisateur = input("Entrez votre nom: ") # demande le nom de l'utilisateur
print("Votre nom est: ", nom_utilisateur) # affichage du nom de l'utilisateur

pays_utilisateur = input("Entrez votre pays: ") # demande le pays de l'utilisateur
print("Votre pays est: ", pays_utilisateur) # affichage du pays de l'utilisateur

age_utilisateur = int(input("Entrez votre age: ")) # demande le age de l'utilisateur
print("Votre age est: ", age_utilisateur) # affichage du age de l'utilisateur

# 14 vérification des mots clés reservés
help('keywords')