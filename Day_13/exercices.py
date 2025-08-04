# Exercices jour 13

# 1 negative and 0
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_0 = [i for i in numbers if i <= 0]
print(negatives_0)

# 2 list of lists of lists 
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [num for lst in list_of_lists for liste in lst for num in liste ]
print(flatten)

# 3 liste of tuples
liste_tuples = [(i, i**0, i**2, i**3, i**4, i**5) for i in range(11)]
print(liste_tuples)

# 4 flatten 
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_countries = [[country.upper(), country[:3].upper(), city.upper()] for [(country, city)] in countries]
print(flatten_countries)

# 5 dictionnaires
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dico = [{'conuntry' : country.upper(), 'city' : city.upper()} for [(country, city)] in countries]
print(dico)

# 6 concatenated 
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],[('Donald', 'Trump')], [('Bill', 'Gates')]]
vide =  ' '
full_name = [first + vide + last for [(first, last)] in names]
print(full_name)