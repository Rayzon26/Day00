def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


import random
random_integers = [random.randint(0, 100) for _ in range(20)]  


print("Tableau avant le tri:", random_integers)


sorted_integers = insertion_sort(random_integers)


print("Tableau après le tri:", sorted_integers)
