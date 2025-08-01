# Dictionnaires

print("\n=== Exercice 1 ===")
# 1. Créer un dictionnaire vide appelé dog
dog = {}
print("Dictionnaire 'dog' vide créé :", dog)

print("\n=== Exercice 2 ===")
# 2. Ajouter des clés au dictionnaire dog
dog['nom'] = 'Rex'
dog['couleur'] = 'Noir'
dog['race'] = 'Berger Allemand'
dog['pattes'] = 4
dog['âge'] = 5
print("Dictionnaire 'dog' après ajout :", dog)

print("\n=== Exercice 3 ===")
# 3. Créer un dictionnaire student avec plusieurs clés
student = {
    'prénom': 'Jean',
    'nom': 'Dupont',
    'genre': 'Masculin',
    'âge': 22,
    'statut_matrimonial': 'Célibataire',
    'compétences': ['Python', 'JavaScript'],
    'pays': 'France',
    'ville': 'Paris',
    'adresse': '123 Rue de la République'
}
print("Dictionnaire 'student' créé :", student)

print("\n=== Exercice 4 ===")
# 4. Obtenir la longueur du dictionnaire student
longueur = len(student)
print("Nombre de clés dans 'student' :", longueur)

print("\n=== Exercice 5 ===")
# 5. Obtenir la valeur des compétences et vérifier le type
competences = student['compétences']
type_competences = type(competences)
print("Compétences :", competences)
print("Type des compétences :", type_competences)
print("Est-ce une liste ?", isinstance(competences, list))

print("\n=== Exercice 6 ===")
# 6. Modifier les compétences en ajoutant de nouvelles
student['compétences'].extend(['HTML', 'CSS'])
print("Compétences après ajout :", student['compétences'])

print("\n=== Exercice 7 ===")
# 7. Obtenir les clés du dictionnaire sous forme de liste
cles = list(student.keys())
print("Clés du dictionnaire :", cles)

print("\n=== Exercice 8 ===")
# 8. Obtenir les valeurs du dictionnaire sous forme de liste
valeurs = list(student.values())
print("Valeurs du dictionnaire :", valeurs)

print("\n=== Exercice 9 ===")
# 9. Convertir le dictionnaire en liste de tuples
items = list(student.items())
print("Dictionnaire converti en tuples :", items)

print("\n=== Exercice 10 ===")
# 10. Supprimer un élément du dictionnaire
element_supprime = student.pop('statut_matrimonial')
print(f"Élément '{'statut_matrimonial'}' supprimé :", element_supprime)
print("Dictionnaire après suppression :", student)

print("\n=== Exercice 11 ===")
# 11. Supprimer un des dictionnaires
print("Avant suppression :")
print("'dog' existe :", 'dog' in locals())
print("'student' existe :", 'student' in locals())

del dog

print("\nAprès suppression de 'dog' :")
print("'dog' existe :", 'dog' in locals())
print("'student' existe :", 'student' in locals())

# Pour éviter une erreur dans les exercices suivants, on recrée dog
dog = {'nom': 'Rex'}  # Recréation minimale pour la démo
