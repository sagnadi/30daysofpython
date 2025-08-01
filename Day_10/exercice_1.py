# Loops

# Exercie 1
# 1 
# for loop
for i in range(11):
    print(i)

# while loop
i = 0
while i < 11:
    print(i)
    i += 1

# 2 
# for loop
for i in range(10, -1, -1):
    print(i)

# while loop
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3 traingle
for i in range(8):
    print("#" * i)

# 4 nested loop
for i in range(8):          
    for j in range(8):     
        print("#", end=" ")   
    print()                 

# 5 Multiplication
for i in range(11):
    print(i, " x ", i, " = ", i*i)

# 6 list
liste = ['Python', 'Numpy','Pandas','Django', 'Flask']
for langage in liste:
    print(langage)

# 7 even numbers
for i in range(101):
    if(i%2 == 0):
        print(i)

# 8 odd numbers
for i in range(101):
    if(i%2 != 0):
        print(i)


