import time
import random

# -------------------------------
# Algoritmo: Quick Sort
# -------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# -------------------------------
# Algoritmo: Merge Sort
# -------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# -------------------------------
# Algoritmo: Counting Sort
# -------------------------------
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# -------------------------------
# Prueba y medición de tiempos
# -------------------------------
# Crear una lista aleatoria
N = 10000  # Puedes subir este número si quieres una prueba más pesada
MAX_VALUE = 1000  # Máximo valor para contar (para Counting Sort)
original_list = [random.randint(0, MAX_VALUE) for _ in range(N)]

# Quick Sort
arr1 = original_list.copy()
start = time.time()
sorted_quick = quick_sort(arr1)
end = time.time()
print(f"Quick Sort tomó {end - start:.6f} segundos.")

# Merge Sort
arr2 = original_list.copy()
start = time.time()
sorted_merge = merge_sort(arr2)
end = time.time()
print(f"Merge Sort tomó {end - start:.6f} segundos.")

# Counting Sort
arr3 = original_list.copy()
start = time.time()
sorted_count = counting_sort(arr3)
end = time.time()
print(f"Counting Sort tomó {end - start:.6f} segundos.")

# Verificar si todas las salidas son iguales
assert sorted_quick == sorted_merge == sorted_count, "¡Los algoritmos no ordenaron igual!"
