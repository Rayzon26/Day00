def check_armstrong():
    
    num = int(input("Entrez un numéro : "))
    
    
    sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
    
   
    if sum_of_cubes == num:
        print(f"{num} est un nombre Armstrong")
    else:
        print(f"{num} n'est pas un nombre Armstrong")


check_armstrong()
