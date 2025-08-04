import random
import string

## Niveau 1

# 1. Génère un identifiant utilisateur aléatoire de 6 caractères
def random_user_id():
    """
    Génère une chaîne aléatoire de 6 caractères pouvant contenir des chiffres et des lettres minuscules.
    """
    characters = string.ascii_lowercase + string.digits  # a-z et 0-9
    return ''.join(random.choice(characters) for _ in range(6))

# 2. Génère des identifiants utilisateur selon les spécifications de l'utilisateur
def user_id_gen_by_user():
    """
    Demande à l'utilisateur le nombre de caractères et le nombre d'IDs à générer.
    Retourne une liste d'identifiants aléatoires.
    """
    # Demande les inputs à l'utilisateur
    char_count = int(input("Nombre de caractères par ID: "))
    id_count = int(input("Nombre d'IDs à générer: "))
    
    characters = string.ascii_letters + string.digits  # a-z, A-Z et 0-9
    ids = []
    for _ in range(id_count):
        # Génère un ID avec le nombre de caractères demandé
        random_id = ''.join(random.choice(characters) for _ in range(char_count))
        ids.append(random_id)
    
    # Retourne les IDs séparés par des nouvelles lignes
    return '\n'.join(ids)

# 3. Génère une couleur RGB aléatoire
def rgb_color_gen():
    """
    Génère une couleur RGB aléatoire sous forme de chaîne 'rgb(r, g, b)'.
    Chaque composante (r, g, b) est un entier entre 0 et 255.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

## Niveau 2

# 1. Génère une liste de couleurs hexadécimales aléatoires
def list_of_hexa_colors(num_colors=1):
    """
    Génère une liste de couleurs hexadécimales aléatoires.
    Chaque couleur est une chaîne de 6 caractères hexadécimaux préfixée par '#'.
    """
    hex_chars = string.hexdigits.lower()[:16]  # 0-9 et a-f
    colors = []
    for _ in range(num_colors):
        # Génère une couleur hexadécimale
        hex_color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        colors.append(hex_color)
    return colors

# 2. Génère une liste de couleurs RGB aléatoires
def list_of_rgb_colors(num_colors=1):
    """
    Génère une liste de couleurs RGB aléatoires.
    Chaque couleur est une chaîne au format 'rgb(r, g, b)'.
    """
    colors = []
    for _ in range(num_colors):
        colors.append(rgb_color_gen())
    return colors

# 3. Génère des couleurs aléatoires selon le type demandé
def generate_colors(color_type, num_colors):
    """
    Génère des couleurs aléatoires selon le type spécifié ('hexa' ou 'rgb').
    Retourne une liste contenant le nombre demandé de couleurs.
    """
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        raise ValueError("Type de couleur non reconnu. Utilisez 'hexa' ou 'rgb'.")

## Niveau 3

# 1. Mélange une liste
def shuffle_list(input_list):
    """
    Prend une liste en entrée et retourne une nouvelle liste mélangée aléatoirement.
    Ne modifie pas la liste originale.
    """
    shuffled = input_list.copy()  # Crée une copie pour ne pas modifier l'original
    random.shuffle(shuffled)
    return shuffled

# 2. Génère un tableau de 7 nombres uniques entre 0 et 9
def unique_random_numbers():
    """
    Génère une liste de 7 nombres aléatoires uniques entre 0 et 9.
    """
    numbers = list(range(10))  # Crée une liste de 0 à 9
    random.shuffle(numbers)    # Mélange la liste
    return numbers[:7]         # Retourne les 7 premiers éléments

## Tests des fonctions

if __name__ == "__main__":
    print("=== Niveau 1 ===")
    print("1. random_user_id():", random_user_id())
    
    print("\n2. user_id_gen_by_user():")
    # Pour tester, vous pouvez décommenter la ligne suivante
    # print(user_id_gen_by_user())  # Entrez par exemple 5 puis 5
    
    print("\n3. rgb_color_gen():", rgb_color_gen())
    
    print("\n=== Niveau 2 ===")
    print("1. list_of_hexa_colors(3):", list_of_hexa_colors(3))
    print("2. list_of_rgb_colors(2):", list_of_rgb_colors(2))
    print("3. generate_colors('hexa', 3):", generate_colors('hexa', 3))
    print("   generate_colors('rgb', 2):", generate_colors('rgb', 2))
    
    print("\n=== Niveau 3 ===")
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("1. shuffle_list([1,2,3,4,5,6,7,8,9]):", shuffle_list(sample_list))
    print("2. unique_random_numbers():", unique_random_numbers())