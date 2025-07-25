# 1 Déclaration de l'age
age = 24

# 2 - Déclaration de la taille
taille = 1.80

# 3 numéro complexe
complexe = 9J

# 4 Calcule de l'air du triangle
base = eval(input("Entrez la base: "))
hauteur = eval(input("Entrez la hauteur: "))
aire_triangle = 0.5 * base * hauteur
print("L'air du triangle est de ", aire_triangle)

# 5 Calcule du périmètre
cote_A = int(input("Entrez le côté A: "))
cote_B = int(input("Entrez le côté B: "))
cote_C = int(input("Entrez le côté C: "))
perimetre = cote_A + cote_B + cote_C
print("Le périmètre du triangle est ", perimetre)

# 6 calcule de surface
longueur = int(input("Entrez la longueur: "))
largeur = int(input("Entrez la largeur: "))
surface= longueur * largeur
print("La surface du triangle est ", surface)

# 7 Air d'un cercle
rayon = int(input("Entrez le rayon du cercle: "))
aire_cercle = 3.14 * rayon**2
circonference = 2 * 3.14 * rayon
print("Le rayon du cercle est {} et la circonférence est {}".format(aire_cercle,circonference))


