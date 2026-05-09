# Bubble Sort Program using User Input

# Taking size of the list
n = int(input("Enter the number of elements: "))

# Taking list elements from user
arr = []

print("Enter the elements:")

for i in range(n):
    element = int(input())
    arr.append(element)

# Bubble Sort
for i in range(n):
    for j in range(0, n - i - 1):

        # Swap if elements are in wrong order
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Display sorted list
print("Sorted List:", arr)