
#### Exercice 2 ####
# 1 sum
sum = 0
for i in range(101):
    sum += i
print("The sum of all numbers is",sum)

# 2 sum even and odd 
even_sum = 0
odd_sum = 0
for i in range(101):
    if(i%2 == 0):
        even_sum += i
    else:
        odd_sum += i
print("The sum of all evens is {}. And the sum of all odds is {}.".format(even_sum,odd_sum))

