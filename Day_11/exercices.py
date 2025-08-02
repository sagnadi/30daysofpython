import math
import statistics
from collections import Counter

# ---------------------------
# Niveau 1
# ---------------------------

print("\n=== Exercice 1.1 ===")
def add_two_numbers(a, b):
    """Additionne deux nombres et retourne le résultat"""
    return a + b

print("3 + 5 =", add_two_numbers(3, 5))

print("\n=== Exercice 1.2 ===")
def area_of_circle(r):
    """Calcule l'aire d'un cercle"""
    return math.pi * r ** 2

print("Aire d'un cercle de rayon 5 :", area_of_circle(5))

print("\n=== Exercice 1.3 ===")
def add_all_nums(*args):
    """Additionne tous les nombres passés en arguments"""
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(f"Attention : {num} n'est pas un nombre et sera ignoré")
    return total

print("Somme de 1, 2, 'a', 3.5 :", add_all_nums(1, 2, 'a', 3.5))

print("\n=== Exercice 1.4 ===")
def convert_celsius_to_fahrenheit(c):
    """Convertit des degrés Celsius en Fahrenheit"""
    return (c * 9/5) + 32

print("20°C =", convert_celsius_to_fahrenheit(20), "°F")

print("\n=== Exercice 1.5 ===")
def check_season(month):
    """Détermine la saison en fonction du mois"""
    month = month.lower()
    if month in ["décembre", "janvier", "février"]:
        return "Hiver"
    elif month in ["mars", "avril", "mai"]:
        return "Printemps"
    elif month in ["juin", "juillet", "août"]:
        return "Été"
    elif month in ["septembre", "octobre", "novembre"]:
        return "Automne"
    else:
        return "Mois inconnu"

print("Saison pour 'juillet' :", check_season("juillet"))

print("\n=== Exercice 1.6 ===")
def calculate_slope(x1, y1, x2, y2):
    """Calcule la pente d'une équation linéaire"""
    return (y2 - y1) / (x2 - x1)

print("Pente entre (1,2) et (3,4) :", calculate_slope(1, 2, 3, 4))

print("\n=== Exercice 1.7 ===")
def solve_quadratic_eqn(a, b, c):
    """Résout une équation quadratique"""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        return "Pas de solution réelle"

print("Solutions de x²-5x+6 :", solve_quadratic_eqn(1, -5, 6))

print("\n=== Exercice 1.8 ===")
def print_list(lst):
    """Affiche chaque élément d'une liste"""
    for item in lst:
        print(item)

print("Éléments de [1, 2, 3] :")
print_list([1, 2, 3])

print("\n=== Exercice 1.9 ===")
def reverse_list(lst):
    """Retourne une liste inversée"""
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print("[1, 2, 3] inversé :", reverse_list([1, 2, 3]))

print("\n=== Exercice 1.10 ===")
def capitalize_list_items(lst):
    """Capitalise chaque élément d'une liste de strings"""
    return [item.capitalize() for item in lst]

print("Capitalisation de ['a', 'b', 'c'] :", capitalize_list_items(['a', 'b', 'c']))

print("\n=== Exercice 1.11 ===")
def add_item(lst, item):
    """Ajoute un élément à une liste"""
    new_list = lst.copy()
    new_list.append(item)
    return new_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print("Ajout de 'Meat' :", add_item(food_staff, 'Meat'))

print("\n=== Exercice 1.12 ===")
def remove_item(lst, item):
    """Retire un élément d'une liste"""
    new_list = lst.copy()
    if item in new_list:
        new_list.remove(item)
    return new_list

print("Retrait de 'Mango' :", remove_item(food_staff, 'Mango'))

print("\n=== Exercice 1.13 ===")
def sum_of_numbers(n):
    """Calcule la somme des nombres de 1 à n"""
    return sum(range(1, n+1))

print("Somme jusqu'à 5 :", sum_of_numbers(5))

print("\n=== Exercice 1.14 ===")
def sum_of_odds(n):
    """Calcule la somme des nombres impairs de 1 à n"""
    return sum(i for i in range(1, n+1) if i % 2 != 0)

print("Somme des impairs jusqu'à 10 :", sum_of_odds(10))

print("\n=== Exercice 1.15 ===")
def sum_of_even(n):
    """Calcule la somme des nombres pairs de 1 à n"""
    return sum(i for i in range(1, n+1) if i % 2 == 0)

print("Somme des pairs jusqu'à 10 :", sum_of_even(10))

# ---------------------------
# Niveau 2
# ---------------------------

print("\n=== Exercice 2.1 ===")
def evens_and_odds(n):
    """Compte les nombres pairs et impairs de 0 à n"""
    evens = len([i for i in range(n+1) if i % 2 == 0])
    odds = n + 1 - evens
    print(f"Nombre de pairs : {evens}")
    print(f"Nombre d'impairs : {odds}")

evens_and_odds(100)

print("\n=== Exercice 2.2 ===")
def factorial(n):
    """Calcule la factorielle de n"""
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorielle de 5 :", factorial(5))

print("\n=== Exercice 2.3 ===")
def is_empty(param):
    """Vérifie si un paramètre est vide"""
    if param:
        return False
    return True

print("Est-ce que [] est vide ?", is_empty([]))

print("\n=== Exercice 2.4 ===")
def calculate_mean(lst):
    """Calcule la moyenne"""
    return statistics.mean(lst)

def calculate_median(lst):
    """Calcule la médiane"""
    return statistics.median(lst)

def calculate_mode(lst):
    """Calcule le mode"""
    return statistics.mode(lst)

def calculate_range(lst):
    """Calcule l'étendue"""
    return max(lst) - min(lst)

def calculate_variance(lst):
    """Calcule la variance"""
    return statistics.variance(lst)

def calculate_std(lst):
    """Calcule l'écart-type"""
    return statistics.stdev(lst)

data = [1, 2, 3, 4, 5, 5, 6]
print("Moyenne :", calculate_mean(data))
print("Médiane :", calculate_median(data))
print("Mode :", calculate_mode(data))
print("Étendue :", calculate_range(data))
print("Variance :", calculate_variance(data))
print("Écart-type :", calculate_std(data))
