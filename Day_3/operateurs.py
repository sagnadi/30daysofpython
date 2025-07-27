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

# 12. Longueur des mots et comparaison fausse
python_len = len('python')
dragon_len = len('dragon')
print(f"12. Longueurs - python:{python_len}, dragon:{dragon_len}")
print("   Comparaison fausse:", python_len == dragon_len + 1)  # Faux intentionnellement

# 13. Vérifier si 'on' est dans les deux mots
print("\n13. 'on' dans les deux mots?:", 'on' in 'python' and 'on' in 'dragon')

# 14. Vérifier présence de 'jargon'
phrase = "I hope this course is not full of jargon"
print("\n14. 'jargon' dans la phrase?:", 'jargon' in phrase)

# 15. Vérifier absence de 'on' (comparaison fausse)
print("\n15. Pas de 'on' dans les deux?:", not ('on' in 'python' and 'on' in 'dragon'))

# 16. Longueur de 'python' et conversions
longueur = len('python')
float_longueur = float(longueur)
str_longueur = str(float_longueur)
print(f"\n16. Longueur: {longueur}, float: {float_longueur}, string: '{str_longueur}'")

# 17. Vérifier si un nombre est pair
nombre = 10
print("\n17. Le nombre", nombre, "est pair?:", nombre % 2 == 0)

# 18. Comparaison division entière
print("\n18. 7//3 == int(2.7)?:", 7//3 == int(2.7))

# 19. Comparaison de types
print("\n19. type('10') == type(10)?:", type('10') == type(10))

# 20. Vérification conversion (avec gestion d'erreur)
try:
    print("\n20. int('9.8') == 10?:", int(float('9.8')) == 10)
except ValueError:
    print("20. Conversion impossible directement de '9.8' en int")

# 21. Calcul de salaire hebdomadaire
print("\n21. Calcul de salaire:")
heures = float(input("Entrez les heures travaillées: "))
taux = float(input("Entrez le taux horaire: "))
salaire = heures * taux
print(f"Votre salaire hebdomadaire est {salaire}")

# 22. Calcul du nombre de secondes vécues
print("\n22. Calcul de secondes vécues:")
annees = int(input("Entrez votre âge en années: "))
secondes = annees * 365 * 24 * 60 * 60  # 1 an = 365j * 24h * 60min * 60s
print(f"Vous avez vécu environ {secondes} secondes")

# 23. Affichage de la table
print("\n23. Table de valeurs:")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

# Version dynamique avec boucle
print("\nVersion dynamique:")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
    
