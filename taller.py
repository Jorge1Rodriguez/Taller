def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        menores = [x for x in arr[1:] if x <= pivot]
        mayores = [x for x in arr[1:] if x > pivot]
        return quick_sort(menores) + [pivot] + quick_sort(mayores)

# Ejemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
print("Lista original:", arr)
sorted_arr = quick_sort(arr)
print("Lista ordenada:", sorted_arr)