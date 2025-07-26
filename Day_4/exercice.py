# 1 Concatenation
mot_1, mot_2,mot_3,mot_4 = 'Thirty', 'Days', 'Of', 'Python'
concatenation = f"{mot_1} {mot_2} {mot_3} {mot_4}"
print(concatenation)

# 2 concatenation 
string_1, string_2,string_3 = 'Coding', 'For' , 'All'
concaten = f"{string_1} {string_2} {string_3}"
print(concaten)

# 3 assignement
company = "Coding For All"

# 4 print company
print(company)

# 5 len of company
print(len(company))

# 6 uppercase
uppercase = company.upper()

# 7 lowercase
lowercase = company.lower()

# 8 formating
capital = "Coding For All".capitalize()
titl = "Coding For All".title()
swap = "Coding For All".swapcase()

# 9 Slicing
slicing = company[7:]
print(slicing)

# 10 checking
checking = company.find("Coding")
if(checking == -1):
    print("Le mot n'existe pas dans la chaine")
else:
    print("Le mot existe dans la chaine")

# 11 replacing
replacing = company.replace("Coding", "Python")
print(replacing)

# 12 change
change = replacing.replace("Python For All", "Python For Everyone")

# 13 spliting
spliting = change.split(" ")

# 14 socio
socio = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(",")

# 15 0 index
all = "Coding For All"
print(all[0])

# 16 last index
print(all[-1])

# 17 10th index
print(all[10])

# 18 acronym 
everyone = "Coding For Everyone"
spliter = everyone.split(" ") # on divise la phrase en mot
acronym = "".join(letter[0] for letter in spliter)
print(acronym)

# 19 abbreviation
splitis = all.split(" ") # on divise la phrase en mot
abbreviation = "".join(first[0] for first in splitis)
print(abbreviation)

# 20 indexing
indexing = all.index("C")

# 21 indexation
indexation = all.index("F")

# 22 reindex
reindex = all.rindex("l")

