def splitToOne(numbers,low , high ):
    if low < high :
        mid = ( low + high ) // 2
        splitToOne(numbers[low:mid-1],low,mid-1)
        splitToOne(numbers[mid+1:high],mid+1,high)
        merge(numbers[low:mid-1],low,mid-1 , numbers[mid+1:high],mid+1,high )
    

