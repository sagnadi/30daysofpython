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

# 8 calcul de la pente, l'ordonnée à l'origine et l'abscisse à l'origine de l'équation y = 2x -2 avec la formule y = mx + b
m = 2
b = -2
pente = 2
y_intercept = (0, b)
x_intercept = (-b/m, 0) # après résolution de l'équaton quand y = 0
print("La pente est {}, l'ordonnée à l'origine est {} et l'abscisse à l'origine est {}".format(pente, x_intercept, y_intercept))

# 9 finding slope and Euclidean distance
from math import sqrt
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Slope = {} and Euclidean distance = {}".format(slope, distance))

# 10 comparaison 
if(pente == slope):
    print("la pente en 8 est égale à celle en 9")
elif(pente>slope):
    print("la pente en 8 est supérieure à celle en 9")
else:
    print("la pente en 8 est inférieure à celle en 9")

# 11 calcule de la fonction
x = 0
for x in range(-10, 10):
    y = x**2 + 6*x + 9
    print(x)
    print(y)
    if(y==0):
        print("y est égale à 0 pour x = ", x)
        break

# 12
    
