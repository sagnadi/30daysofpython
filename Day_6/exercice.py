# EXERCIExerciceCES 1
# 1. Créer un tuple vide
tuple_vide = ()
print(tuple_vide)

# 2. Tuple des frères et sœurs
freres = ('Jean', 'Paul')
soeurs = ('Marie', 'Claire', 'Anne')
print("Frères:", freres, "Sœurs:", soeurs)

# 3. Joindre les tuples
fratrie = freres + soeurs
print("Fratrie complète:", fratrie)

# 4. Nombre de frères et sœurs
nb_fratrie = len(fratrie)
print("Nombre de frères et sœurs:", nb_fratrie)

# 5. Ajouter parents (on convertit en liste pour modifier)
liste_famille = list(fratrie)
liste_famille.extend(['Pierre', 'Sophie'])  # Ajout parents
famille = tuple(liste_famille)
print("Famille complète:", famille)

# EXERCICES 2
# 1. Déballer la famille
*freres_soeurs, pere, mere = famille
print("Parents déballés:")
print("Enfants:", freres_soeurs)
print("Père:", pere, "Mère:", mere)

# 2. Tuples nourriture
fruits = ('pomme', 'banane', 'orange')
legumes = ('carotte', 'épinard', 'brocoli')
produits_animaux = ('lait', 'fromage', 'œufs')
aliments_tp = fruits + legumes + produits_animaux
print("Tous les aliments (tuple):", aliments_tp)

# 3. Conversion tuple -> liste
aliments_liste = list(aliments_tp)
print("Version liste:", aliments_liste)

# 4. Élément(s) du milieu
milieu = len(aliments_tp) // 2
if len(aliments_tp) % 2 == 1:
    print("Aliment du milieu:", aliments_tp[milieu])
else:
    print("Aliments du milieu:", aliments_tp[milieu-1:milieu+1])

# 5. Premiers et derniers éléments
print("Premiers 3:", aliments_liste[:3])
print("   Derniers 3:", aliments_liste[-3:])

# 6. Supprimer le tuple
del aliments_tp
print("Tuple supprimé - si on tente d'y accéder, ça générera une erreur")

# 7. Vérification d'appartenance
pays_nordiques = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Vérifications:")
print("   Estonie est nordique?", 'Estonia' in pays_nordiques)
print("   Islande est nordique?", 'Iceland' in pays_nordiques)