import sys
import bubble_sort
numbers=[]

for i in range(1, len(sys.argv)):
   numbers.append(int(sys.argv[i]))

print('Sorted List', bubble_sort.bubbleSort_optimised(len(numbers),numbers))

