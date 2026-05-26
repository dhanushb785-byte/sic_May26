def selectionSort(numbers):
    for i in range(len(numbers)):
        small_number = numbers[i]
        index = i
        for j in range(i+1,len(numbers)):
            if numbers[j] < small_number:
                small_number = numbers[j]
                index = j
        
      
        numbers[i] , numbers[index] = numbers[index] ,  numbers[i]
    return numbers
    


        

