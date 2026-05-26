import sys
import Quick_Sort as qs
numbers=[int(value) for value in range(1 , len(sys.argv))]
print('Elements Befor QuickSort=',numbers)
sortedNumebrs = qs.quickSort(numbers , 0 , len(numbers))
print('Elements after QuickSort=',sortedNumbers)