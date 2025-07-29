# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercice 1
# 1 find lenght
longueur_it = len(it_companies)
print(longueur_it)

# 2 adding
it_companies.add("'Twitter'")
print(it_companies)

# 3 insert
it_companies.update(["Tesla", "T-Mobile", "Exabeam"])
print(it_companies)

# 4 remove 
it_companies.remove("IBM")
print(it_companies)

# 5 la différence entre remove et discard est que remove() retourne une erreur si l'élément à supprimé n'est pas trouvé dans le set mais discard ne retourne pas d'erreur 

# Exercice 2
# 1 Join
C = A.union(B)
print(C)

# 2 intersection
D = A.intersection(B)
print(D)

# 3 Subset 
if A.issubset(B):
    print("Oui A est un subset de B")
else: 
    print("Non A n'est pas un subset de B")

# 4 Disjoint
if A.isdisjoint(B):
    print("Ou A et B sont disjoints")
else:
    print("Non A et B ne sont pas disjoint")

# 5 Join 
#E = A.union(B)
#F = B.update(A)
#print(F)

# 6 symetric difference
G = A.symmetric_difference(B)
print(G)

# 7 delete
del(A,B)


# Exercice 3
# 1 list to set 
set_age = set(age)
print(set_age)

if (len(age) > len(set_age)):
    print("La liste est plus longue que le set")
elif(len(age) == len(set_age)):
    print("La liste et le set ont la meme longueur")
else:
    print("Le set est plus long que la liste")

# 2 En Python, une string (chaîne de caractères) est une séquence immuable de caractères utilisée pour stocker du texte, comme nom = "Alice". Une list (liste) est une collection mutable et ordonnée d'éléments modifiables, définie entre crochets : liste = [1, 2, 3]. Un tuple est similaire à une liste mais immuable, déclaré avec des parenthèses : tuple = (1, 2, 3), idéal pour des données fixes. Un set (ensemble) est une collection non ordonnée et mutable d'éléments uniques, utilisé avec des accolades : ensemble = {1, 2, 3}, parfait pour éliminer les doublons ou tester des appartenances.

# 3 Unique words
phrase = "I am a teacher and I love to inspire and teach people"
words = phrase.split(" ")
unique_words = set(words)
print("La phrase contient {} mots uniques.".format(len(unique_words)))