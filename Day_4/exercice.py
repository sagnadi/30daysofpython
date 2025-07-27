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

# 23
sentence = "You cannot end a sentence with because because because is a conjunction"
first_because = sentence.find("because")
print("Première position de 'because' :", first_because)

# 24
last_because = sentence.rindex("because")
print("Dernière position de 'because' :", last_because)

# 25
start = sentence.find("because")
end = sentence.rfind("because") + len("because")
sliced = sentence[start:end]
print("Extrait :", sliced)

# 26
pos = sentence.find("because")
print("Position :", pos)

# 27
start = sentence.find("because")
end = sentence.rfind("because") + len("because")
print("Sliced phrase:", sentence[start:end])

# 28
text = "Coding For All"
print(text.startswith("Coding"))

# 29
print(text.endswith("coding"))

# 30
text_with_spaces = "   Coding For All   "
cleaned = text_with_spaces.strip()
print(f"'{cleaned}'")

# 31
print("30DaysOfPython".isidentifier())        
print("thirty_days_of_python".isidentifier())  


# 32
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined = ' # '.join(libs)
print(joined)

# 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

# 36
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))       # Format à 2 décimales
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
