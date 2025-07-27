# ----------------------------
# EXERCICES SUR LES LISTES PYTHON
# ----------------------------

# 1. Déclarer une liste vide
liste_vide = []
print("1. Liste vide:", liste_vide)

# 2. Déclarer une liste avec plus de 5 éléments
liste_fruits = ["pomme", "banane", "orange", "kiwi", "mangue", "fraise"]
print("\n2. Liste de fruits:", liste_fruits)

# 3. Trouver la longueur de la liste
nombre_fruits = len(liste_fruits)
print("\n3. Nombre de fruits:", nombre_fruits)

# 4. Obtenir le premier, milieu et dernier élément
premier = liste_fruits[0]
milieu = liste_fruits[len(liste_fruits)//2]
dernier = liste_fruits[-1]
print("\n4. Premier:", premier, "/ Milieu:", milieu, "/ Dernier:", dernier)

# 5. Liste avec différents types de données
donnees_melangees = ["Marie", 28, 1.68, "célibataire", "10 Rue des Fleurs"]
print("\n5. Données mélangées:", donnees_melangees)

# 6. Liste d'entreprises technologiques
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("\n6. Sociétés tech:", it_companies)

# 7. Afficher la liste
print("\n7. Liste complète:")
print(it_companies)

# 8. Afficher le nombre d'entreprises
print("\n8. Nombre de sociétés:", len(it_companies))

# 9. Afficher première, milieu et dernière société
print("\n9. Première:", it_companies[0], 
      "/ Milieu:", it_companies[len(it_companies)//2], 
      "/ Dernière:", it_companies[-1])

# 10. Modifier une société
it_companies[1] = "Alphabet"
print("\n10. Après modification:")
print(it_companies)

# 11. Ajouter une société
it_companies.append("Netflix")
print("\n11. Après ajout:")
print(it_companies)

# 12. Insérer au milieu
it_companies.insert(len(it_companies)//2, "Twitter")
print("\n12. Après insertion au milieu:")
print(it_companies)

# 13. Mettre une société en majuscules (sauf IBM)
for i, societe in enumerate(it_companies):
    if societe != "IBM":
        it_companies[i] = societe.upper()
        break
print("\n13. Après majuscules:")
print(it_companies)

# 14. Joindre avec séparateur
print("\n14. Chaîne jointe:")
print("#; ".join(it_companies))

# 15. Vérifier existence
recherche = "Google"
print(f"\n15. {recherche} existe? {recherche in it_companies}")

# 16. Trier la liste
it_companies.sort()
print("\n16. Liste triée:")
print(it_companies)

# 17. Inverser l'ordre
it_companies.reverse()
print("\n17. Liste inversée:")
print(it_companies)

# 18. Premières 3 sociétés
print("\n18. 3 premières:", it_companies[:3])

# 19. 3 dernières sociétés
print("\n19. 3 dernières:", it_companies[-3:])

# 20. Société(s) du milieu
milieu = len(it_companies)//2
if len(it_companies) % 2 == 1:
    print("\n20. Société du milieu:", it_companies[milieu])
else:
    print("\n20. Sociétés du milieu:", it_companies[milieu-1:milieu+1])

# 21. Supprimer la première
premiere = it_companies.pop(0)
print(f"\n21. Après suppression de {premiere}:")
print(it_companies)

# 22. Supprimer au milieu
milieu = len(it_companies)//2
if len(it_companies) % 2 == 1:
    supprime = it_companies.pop(milieu)
    print(f"\n22. Suppression de {supprime} au milieu")
else:
    supprime1 = it_companies.pop(milieu-1)
    supprime2 = it_companies.pop(milieu-1)
    print(f"\n22. Suppression de {supprime1} et {supprime2} au milieu")
print("Résultat:", it_companies)

# 23. Supprimer la dernière
derniere = it_companies.pop()
print(f"\n23. Après suppression de {derniere}:")
print(it_companies)

# 24. Vider la liste
it_companies.clear()
print("\n24. Liste vidée:", it_companies)

# 25. Détruire la liste
del it_companies
print("\n25. Liste détruite - si vous essayez d'y accéder, vous aurez une erreur")

# 26. Joindre les listes front_end et back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
liste_complete = front_end + back_end
print("26. Liste complète après jointure (méthode +):", liste_complete)

# 27. Copie et insertion dans full_stack
full_stack = front_end + back_end
print("\n27. full_stack avant insertion:", full_stack)

# Trouver l'index de 'Redux' pour insérer après
index_redux = full_stack.index('Redux')

# Insertion de 'Python' et 'SQL' après 'Redux'
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')
print("27. full_stack après insertion:", full_stack)

# Exercice 2
# 1. Manipulation des âges
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a. Trier la liste et trouver min et max
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(f"1a. Âges triés: {ages}, Min: {min_age}, Max: {max_age}")

# b. Ajouter min et max à nouveau
ages.extend([min_age, max_age])
print(f"1b. Après ajout: {ages}")

# c. Trouver l'âge médian
n = len(ages)
if n % 2 == 1:
    median = ages[n//2]
else:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
print(f"1c. Âge médian: {median}")

# d. Trouver la moyenne d'âge
average = sum(ages) / len(ages)
print(f"1d. Moyenne d'âge: {average:.2f}")

# e. Trouver l'étendue des âges
range_ages = max_age - min_age
print(f"1e. Étendue des âges: {range_ages}")

# f. Comparer (min - moyenne) et (max - moyenne)
diff_min = abs(min_age - average)
diff_max = abs(max_age - average)
print(f"1f. Différences: min-moyenne={diff_min:.2f}, max-moyenne={diff_max:.2f}")

# 2. Pays du milieu
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

mid = len(countries) // 2
if len(countries) % 2 == 1:
    middle_country = countries[mid]
    print(f"\n2. Pays du milieu: {middle_country}")
else:
    middle_countries = countries[mid-1:mid+1]
    print(f"\n2. Pays du milieu: {middle_countries}")

# 3. Diviser la liste de pays
if len(countries) % 2 == 0:
    part1 = countries[:len(countries)//2]
    part2 = countries[len(countries)//2:]
else:
    part1 = countries[:len(countries)//2 + 1]
    part2 = countries[len(countries)//2 + 1:]
print(f"\n3. Division des pays:")
print(f"Première partie ({len(part1)}): {part1}")
print(f"Seconde partie ({len(part2)}): {part2}")

# 4. Déballage des pays
pays_scandinaves = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
premier, deuxieme, troisieme, *scandinaves = pays_scandinaves
print(f"\n4. Déballage:")
print(f"3 premiers pays: {premier}, {deuxieme}, {troisieme}")
print(f"Pays scandinaves: {scandinaves}")