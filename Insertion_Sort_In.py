import sys
import Insertion_Sort as ins
elements=[]
for i in range(1,len(sys.argv)):
    elements.append(sys.argv[i])

print('Sosrted Elements = ',ins.insertionSort(elements))