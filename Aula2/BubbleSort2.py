# Bubble Sort sem usar uma função separada com uma variável temporária

# Lista de exemplo a ser ordenada
arr = [64, 25, 12, 22, 11]
print("Lista NÃO ordenada:", arr)
# Número de elementos na lista
n = len(arr)

# Realiza a ordenação pelo Bubble Sort
for i in range(n):
    for j in range(0, n - i - 1):
        # Use uma variável temporária (tmp) para trocar os elementos
        if arr[j] > arr[j + 1]:
            tmp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = tmp

# Exibe a lista ordenada
print("Lista ordenada:", arr)
