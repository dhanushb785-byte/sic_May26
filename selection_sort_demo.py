import selection_sort as ss
import sys
numbers = []
for i in range(1,len(sys.argv)):
    numbers.append(int(sys.argv[i]))

sortedNumbers = ss.selectionSort(numbers)
print('Sorted Array:',sortedNumbers)

