# Binary Search Program
# User enters size, elements, target element
# Program sorts the list and performs binary search

# Taking size of the list
n = int(input("Enter the size of the list: "))

# Taking list elements
arr = []

print("Enter the elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

# Sorting the list
arr.sort()

print("Sorted List:", arr)

# Element to search
target = int(input("Enter the element to search: "))

# Binary Search Function
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # If element found
        if arr[mid] == target:
            return mid

        # If target is greater, search right half
        elif arr[mid] < target:
            low = mid + 1

        # If target is smaller, search left half
        else:
            high = mid - 1

    return -1


# Calling binary search
result = binary_search(arr, target)

# Displaying result
if result != -1:
    print(f"Element {target} found at position  {result+1}")
else:
    print(f"Element {target} not found in the list")