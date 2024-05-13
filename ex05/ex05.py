def selection_sort_desc(arr):
    n = len(arr)
    
    for i in range(n):
        
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
       
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


import random
random_integers = [random.randint(0, 100) for _ in range(20)]  


print("Tableau avant le tri:", random_integers)


sorted_integers = selection_sort_desc(random_integers)


print("Tableau après le tri:", sorted_integers)
