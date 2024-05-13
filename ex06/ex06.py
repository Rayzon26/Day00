def custom_len(string):
    count = 0  
    for char in string:
        count += 1  
    return count  


input_string = "Bonjour ! Comment ça va ?"
length = custom_len(input_string)
print("La longueur de la chaîne est :", length)
