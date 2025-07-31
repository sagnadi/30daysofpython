# Conditions

# Exercice 1

print("\n=== Exercice 1.1 ===")
# 1. Vérification de l'âge pour conduire
age = int(input("Entrez votre âge : "))
if age >= 18:
    print("Vous êtes assez âgé pour apprendre à conduire.")
else:
    annees_manquantes = 18 - age
    print(f"Vous devez attendre encore {annees_manquantes} ans pour apprendre à conduire.")

print("\n=== Exercice 1.2 ===")
# 2. Comparaison d'âges
mon_age = 25  # valeur arbitraire
votre_age = int(input("Entrez votre âge : "))

if votre_age > mon_age:
    difference = votre_age - mon_age
    if difference == 1:
        print(f"Vous avez {difference} an de plus que moi.")
    else:
        print(f"Vous avez {difference} ans de plus que moi.")
elif votre_age < mon_age:
    difference = mon_age - votre_age
    if difference == 1:
        print(f"J'ai {difference} an de plus que vous.")
    else:
        print(f"J'ai {difference} ans de plus que vous.")
else:
    print("Nous avons le même âge !")

print("\n=== Exercice 1.3 ===")
# 3. Comparaison de deux nombres
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

if a > b:
    print(f"{a} est plus grand que {b}")
elif a < b:
    print(f"{a} est plus petit que {b}")
else:
    print(f"{a} est égal à {b}")

# Exercice 2

print("\n=== Exercice 2.1 ===")
# 1. Attribution de notes
score = float(input("Entrez le score de l'étudiant (0-100) : "))

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print(f"La note correspondante est : {grade}")

print("\n=== Exercice 2.2 ===")
# 2. Détermination de la saison
mois = input("Entrez un mois : ").lower()

if mois in ["septembre", "octobre", "novembre"]:
    saison = "Automne"
elif mois in ["décembre", "janvier", "février"]:
    saison = "Hiver"
elif mois in ["mars", "avril", "mai"]:
    saison = "Printemps"
elif mois in ["juin", "juillet", "aout"]:
    saison = "Été"
else:
    saison = "Inconnue"

print(f"La saison correspondante est : {saison}")

print("\n=== Exercice 2.3 ===")
# 3. Gestion de liste de fruits
fruits = ['banane', 'orange', 'mangue', 'citron']
nouveau_fruit = input("Entrez un fruit : ").lower()

if nouveau_fruit in fruits:
    print("Ce fruit existe déjà dans la liste.")
else:
    fruits.append(nouveau_fruit)
    print("Liste de fruits mise à jour :", fruits)

# Exercice 3

print("\n=== Exercice 3.1 ===")
# 1. Manipulation de dictionnaire
personne = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finlande',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Rue de l\'espace',
        'zipcode': '02210'
    }
}

# a. Vérification de la clé 'skills' et impression de la compétence du milieu
if 'skills' in personne:
    skills = personne['skills']
    milieu = len(skills) // 2
    print("Compétence du milieu :", skills[milieu])

# b. Vérification de la compétence Python
if 'skills' in personne and 'Python' in personne['skills']:
    print("La personne a des compétences en Python")

# c. Détermination du type de développeur
skills = personne['skills']
if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print("C'est un développeur front-end")
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print("C'est un développeur back-end")
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("C'est un développeur fullstack")
else:
    print("Titre inconnu")

# d. Information sur le statut matrimonial et le pays
if personne['is_married'] and personne['country'] == 'Finlande':
    nom_complet = f"{personne['first_name']} {personne['last_name']}"
    print(f"{nom_complet} vit en {personne['country']}. Il est marié.")
