def insertionSort(unsortedElements):
    for i in range(1,len(unsortedElements)):
        j = i - 1
        key = unsortedElements[i]
        while j>=0 and unsortedElements[j] > key:
            unsortedElements[j+1] = unsortedElements[j]
            j  = j - 1
        unsortedElements[j+1] = key
    return unsortedElements
