def print_star_pyramid():
    
    n = int(input("Entrez le nombre de lignes pour la pyramide d'étoiles: "))
    while n <= 0:
        n = int(input("S'il vous plaît, entrez un nombre positif: "))

    
    for i in range(1, n + 1):
        
        spaces = ' ' * (n - i)
        
        stars = '* ' * (2 * i - 1)
        
        print(spaces + stars.strip())


print_star_pyramid()
