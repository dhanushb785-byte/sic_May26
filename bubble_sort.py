
def bubbleSort_optimised(size,elemnts):
    for i in range(size-2):
        sorted = True
        for j in range(size-2-i):
            if elemnts[j] > elemnts[j+1] :
                sorted = False
                elemnts[j]  ,  elemnts[j+1] = elemnts[j+1] , elemnts[j] 
        if sorted :
            break
    return elemnts
