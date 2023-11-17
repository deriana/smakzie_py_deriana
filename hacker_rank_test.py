def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice_points += 1
        elif a[i] < b[i]:
            bob_points += 1
    
    return (alice_points, bob_points)

# Contoh penggunaan
a = [5, 6, 7]
b = [3, 6, 10]

result = compareTriplets(a, b)
print(result)  # Outputnya adalah (1, 1), yang berarti Alice dan Bob masing-masing mendapatkan 1 poin.
