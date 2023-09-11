# Bubble Sort without using a separate function

# Sample list to be sorted
arr = [64, 25, 12, 22, 11]
print("Array is:", arr)

# Number of elements in the list
n = len(arr)

# Perform the bubble sort
for i in range(n):
    for j in range(0, n - i - 1):
        # Swap if the element found is greater
        # than the next element

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr[j], arr[j + 1])
# Display the sorted array
print("Sorted array is:", arr)
