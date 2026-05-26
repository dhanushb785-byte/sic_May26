import Partition_Array as pa

def quickSort(numbers , low , high ):
    key = pa.partitionArray(numbers)
    if low < high :
        quickSort(numbers , key - 1 , high )
        quickSort(numbers , low , key-1 )
   